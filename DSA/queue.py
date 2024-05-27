class queue:
    def __init__(self):
        self.items = []
        self.size = 9

    def insertToQueue(self,value):
        if(len(self.items) == self.size):
            print("queue full ")
        else:    
            self.items.append(value) 
    
    def deleteFromQueue(self):
        if(len(self.items) == 0):
            print("no element cant delete ")
        else:    
            self.items.pop(0)


queueobj = queue()            
queueobj.insertToQueue(10)
queueobj.insertToQueue(90)
queueobj.insertToQueue(0)
queueobj.insertToQueue(70)
queueobj.deleteFromQueue()
print(queueobj.items)
print(len(queueobj.items)) 