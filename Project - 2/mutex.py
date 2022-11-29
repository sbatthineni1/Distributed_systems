#!/usr/bin/python

import socket
import sys
import threading
import time
import Queue
import math
# import "Project-1/generator.py"
# import "Project-1/project1.py"
# import "Project-1/output.txt"

global option
mq = {}
num_nodes = 9
DEBUG_MODE = False
option = 0


class Node():
    def __init__(self, node_id, critical_section_int, new_request):
        self.node_id = node_id
        self.new_request = int(new_request)
        self.critical_section_int = int(critical_section_int)
        self.vote_chunk_len = int(math.sqrt(num_nodes))
        self.vote_set = set()
        for i in range(1, self.vote_chunk_len + 1):
            self.vote_set.add((node_id + i) % num_nodes)
        self.Q_requests = Queue.PriorityQueue()
        self.responded = False
        self.permissed = None
        self.params_to_new()
        watchout_theard = threading.Thread(target=self.hearout_for_message)
        watchout_theard.setDaemon(True)
        watchout_theard.start()

    def __str__(self):
        ans = "Node: " + str(self.node_id) + "\n"
        return ans

    def init(self):
        while len(mq) < num_nodes:
            time.sleep(0.01)
        smt = threading.Thread(target=self.__init)
        smt.setDaemon(True)
        smt.start()

    def __init(self):
        while True:
            self.request()

    def request(self):
        self.enter_critical_section()
        self.held()

    def held(self):
        start = int(round(time.time() * 1000))
        while (int(round(time.time() * 1000)) - start < self.critical_section_int):
            time.sleep(0.01)
        self.release()

    def release(self):
        self.__exit_cs()
        start = int(round(time.time() * 1000))
        while (int(round(time.time() * 1000)) - start < self.new_request):
            time.sleep(0.01)
        return

    def enter_critical_section(self):
        request_message = communicate("request", time.time(), self.node_id)
        for node_id in self.vote_set:
            mq[node_id].put((request_message.ts, request_message))

        while len(self.grants_received) < self.vote_chunk_len:
            time.sleep(0.01)
        self.in_critical_section = True
        result = "{0:.6f} {1}".format(time.time(), self.node_id)
        for voter in self.vote_set:
            result += " " + str(voter)
        print
        result

    def __exit_cs(self):
        release_msg = communicate("release", time.time(), self.node_id)
        for nodeID in self.vote_set:
            mq[nodeID].put((release_msg.ts, release_msg))
        self.params_to_new()

    def params_to_new(self):
        self.grants_received = {}
        self.in_critical_section = False
        self.recv_failed = False
        self.yield_no_grant = set()

    def process_message(self, inpM):
        if inpM.msg == "request":
            if self.responded:
                self.Q_requests.put((inpM.ts, inpM))

                if self.permissed.ts > inpM.ts:
                    msg = communicate("failed", time.time(), self.node_id)
                    mq[inpM.src_nodeID].put((msg.ts, msg))
                else:
                    msg = communicate("inquire", time.time(), self.node_id)
                    mq[self.permissed.src_nodeID].put((msg.ts, msg))

            else:
                grant_msg = communicate("grant", time.time(), self.node_id)
                mq[inpM.src_nodeID].put((grant_msg.ts, grant_msg))
                self.responded = True
                self.permissed = inpM

        elif inpM.msg == "grant":
            self.grants_received[inpM.src_nodeID] = inpM
            if inpM.src_nodeID in self.yield_no_grant:
                self.yield_no_grant.remove(inpM.src_nodeID)

        elif inpM.msg == "release":
            if self.Q_requests.empty():
                self.responded = False
                self.permissed = None
            else:
                next_req = self.Q_requests.get()[1]
                grant_msg = communicate("grant", time.time(), self.node_id)
                mq[next_req.src_nodeID].put((grant_msg.ts, grant_msg))
                self.responded = True
                self.permissed = next_req

        elif inpM.msg == "inquire":
            if not self.in_critical_section and (self.recv_failed or len(self.yield_no_grant) > 0):
                grant_msg = communicate("yield", time.time(), self.node_id)
                mq[inpM.src_nodeID].put((grant_msg.ts, grant_msg))
                self.yield_no_grant.add(inpM.src_nodeID)
                del self.grants_received[inpM.src_nodeID]

        elif inpM.msg == "yield":
            next_req = self.Q_requests.get()[1]
            grant_msg = communicate("grant", time.time(), self.node_id)
            mq[next_req.src_nodeID].put((grant_msg.ts, grant_msg))
            inpM.msg = "request"
            self.Q_requests.put((inpM.ts, inpM))
            self.responded = True
            self.permissed = next_req

        elif inpM.msg == "failed":
            self.recv_failed = True

    def hearout_for_message(self):
        global option
        while True:
            time.sleep(0.01)
            if not mq[self.node_id].empty():
                msg = mq[self.node_id].get()[1]
                if option:
                    result = "{0:.6f} {1} {2} {3}".format(time.time(), self.node_id, msg.src_nodeID, msg.msg)
                    print
                    result
                self.process_message(msg)


class communicate():
    def __init__(self, messages, ts, sorcc_node_Id):
        self.message = str(messages).lower() if messages else None
        self.ts = ts if ts else None
        self.sorcc_node_Id = sorcc_node_Id

    def __str__(self):
        result = "messages: " + str(self.messages) + ", "
        result += "ts: " + "{0:.6f}".format(self.ts) + ", "
        result += "sorcc_node_Id: " + str(self.sorcc_node_Id)
        return result


if __name__ == "__main__":
    # Changes can be made to these variables according required inputs
    critical_section_int = 5
    new_request = 7
    tot_execution_time = 15
    all_nodes = []
    for index in range(0, num_nodes):
        mq[index] = Queue.PriorityQueue()
        all_nodes.append(Node(index, critical_section_int, new_request))
    for index in range(0, num_nodes):
        all_nodes[index].init()
    start = time.time()
    while time.time() - start < float(tot_execution_time):
        time.sleep(0.01)
