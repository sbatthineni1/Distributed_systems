def initializeSemaphores():
    #return thread id
    pass


def fillList(value):
    #Fills the list
    pass

def emptyList(value):
     #empty the list
    pass

def showList(thread_num):
    #Shows the list
    pass

def threadMutexDestroy(thread_num):
    #Destroy tread mutex
    pass

def initializeList(thread_num):
    #This function initialises the list
    pass

def semDestroy(thread_num):
    #semaphore destroy
    pass

def initializeMutex(thread_num):
    #Shows the list
    pass

def Traverse(thread_num):
    #Shows the list
    pass


def threadCreate(thread_num):
    #Shows the list
    pass

def threadJoin(thread_num):
    #Shows the list
    pass
 


if __name__ ==  "__main__":
 

    initializeMutex()  
    initializeSemaphores() #it return thread id  
    param =  [0, 1, 2, 3, 4]   
    #array used to pass parameter to thread functions  
     
    for i in range(5):
        #creating 5 threads. Each thread enters one number (0-4) in the list   
        pass

    for i in range(0,5):
        #creating 5 threads. Each thread removes one number (0-4) from the list  
        threadCreate()
        pass
     

    for i in range(10):
        threadJoin() 


    threadMutexDestroy() 
    semDestroy() 
    semDestroy() 
    Traverse() 

