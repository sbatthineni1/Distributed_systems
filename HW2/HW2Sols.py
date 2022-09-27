
'''Imagine a very long bridge across the Mississippi River. A car will take upwards of 15
minutes to cross this bridge. Due to construction, the bridge has been reduced to a single
lane that has to be shared by traffic in both the west-east and the east-west direction. It is
obviously not possible to allow traffic in both directions simultaneously and so a special
traffic control mechanism is installed with the following rules:
• An arriving car will have to wait if the bridge is currently occupied by one or more
cars moving in the opposite direction.
• Multiple cars are allowed to cross the bridge in the same direction (otherwise there
would be little bridge utilization and arriving cars would have to wait a long time).
• In order to avoid starvation, the entry of cars onto the bridge in one direction must be
stopped after a batch of k cars has entered the bridge to allow traffic in the opposite
direction if there are any cars waiting.
• If there are no cars, the bridge is open in both directions and the first arriving car will
determine the direction of traffic.
Viewing each car as a process that is traveling in West-East (WE) or East-West (EW)
direction, develop a MONITOR that implements the rules listed above. You MONITOR
must use the monitor procedures Enter_WE(), Enter_EW(), Exit_WE(), Exit_EW(), to
be executed when a car enters and exits the bridge.
Your solution must show all the necessary MONITOR variables and the condition
variables and must not unnecessarily restrict vehicles to cross the bridge, must be
deadlock free, and must not starve traffic in any direction. '''

# Lemme run an infinite loop
# The meaning of this infinite loop is that the vehicles will keep on coming towards the bridge

#An arriving car will have to wait if the bridge is currently occupied by one or more 
#cars moving in the opposite direction.


bridgeTaken = "No"
K = 25

class Moniter:
    def __init__(self):
            self.red = False;
            self.green = True;
            self.vehiclesWaiting = False;
            self.vehicleCount = 0;
            self.sawAVehicle = False;

    def setRed(self, value):
        self.red = value

    def setGreen(self,value):
        self.green = value;

    def setVehiclesWaiting(self,value):
        self.vehiclesWaiting = value

    def setVehicleCount(self,value):
        self.vehicleCount = value

    def setSawAVehicle(self,value):
        self.sawAVehicle = value

    def enter():
        print("vehicle Entered")
    

    def exit():
        print("vehicle exited")

    
def toggleBridgeTaken():
    bridgeTaken ^= True

def brideTakenBy():
    # This method retunrs 
    # E->W : If the bridge is taken by vehicles moving from E->W
    # W->E : If the bridge is taken by vehicles moving from W->E
    Toggle(TakenBy)


def wait():
    # This module asks the vehicle to wait
    # waiting 15 minutes
    wait()
    pass

def setBothMonitorsGreen(moniterEW,moniterWE):
    moniterEW.green = True
    moniterWE.green = True

def checkForIncomingVehicles(moniterEW,moniterWE):
    if(moniterEW.sawAVehicle == True):
        moniterWE.red = True
        bridgeTaken = "Yes"
        return moniterEW,moniterWE
    elif(moniterWE.sawAVehicle == True):
        moniterEW.red = True
        bridgeTaken = "Yes"
        return moniterWE,moniterEW
    return None



if __name__ == '__main__':
    # If there are no cars, the bridge is open in both directions and the first arriving car will
    # determine the direction of traffic.

    moniterEW = Moniter();
    moniterWE = Moniter();


    while(1):
        if( bridgeTaken == "No" ):
            setBothMonitorsGreen(moniterEW,moniterWE)
            currentUser,waitingUser = checkForIncomingVehicles(moniterEW,moniterWE)

            if(currentUser != None):

                while currentUser.vehicleCount < K and currentUser.sawAVehicle == True :
                    currentUser.green = True                    
                else:
                    currentUser.reset()
                    wait()
                    bridgeTaken = "No"
            









                



