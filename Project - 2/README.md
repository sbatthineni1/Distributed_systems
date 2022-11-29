# Group - 9 
# Team details
# Group - 9

[//]: # (Students Details: )

[//]: # (Name                 Panther-ID)

[//]: # (Shilpa Battineni     002670546)

[//]: # (Supriya Parvatham    002671494)

[//]: # (Nikhil Mukund Karve  002575462)

[//]: # (Kiran Reddy          002678089)


Approach: Developing the node generation part and the node communication in the same script.
# enivironment:

1)Pycharm
2)Python3
3)Install requirments.txt

# Setup
Step - 1 :Clone the project
Step - 2 : Cd to the required directory
step -3 : run the code with the required command line arguments
to make this step a little easy. you can input the required arguments in the code as well.

# Algorithm explained:

Step -1 : read all the required inputs lie size and all <br>
Step - 2: creating the priority queue for each <br>
Step - 3 : creating the nodes <br>
Step - 4 : creating the set part using the internal class methods of the main class node <br>
Step -5 : initiating the node communication part <br>
Step -6 : internall class methods handle the crtical section access <br>
for index in range(0, num_nodes):
        mq[index] = Queue.PriorityQueue()
        all_nodes.append(Node(index, critical_section_int, new_request))

<br>

Step - 7 : now for all such generated nodes <br>
    for index in range(0, num_nodes):
        all_nodes[index].init() <br>

Created a list and storing all the node obejects in the list. <br>

Creating the communication where the message modules is effectively handled. <br>





    class communicate():
    def __init__(self, messages, ts, sorcc_node_Id):
        // Initiating the communication module
        self.sorcc_node_Id = sorcc_node_Id
        //
    def __str__(self):
        result = "messages: " + str(self.messages) + ", "
        result += "ts: " + "{0:.6f}".format(self.ts) + ", "
        result += "sorcc_node_Id: " + str(self.sorcc_node_Id)
        return 


