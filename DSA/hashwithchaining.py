# HASH FUNCTION TO FIND LOCATION TO STORE VALUE
#  WE SUM UP THE ASCII OF A PARTICULAY KEY AND THEN MODULUS OF IT IS TKAEN TO FIND HASH VALUE

class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]  # instead of none, key value pair beacuse chaingn use linke dlist


    def gethash(self,key):  # TO find hash of a key    ......key is mar 1 and value is 100 ( mar 1,100)
        sum = 0
        for char in key:
            sum  = sum + ord(char)   # ord used to get ascii
        return sum % self.MAX

    def add(self,key,value):    # can use set item and getitem for adding and geting value from hash
        hash = self.gethash(key)

        Found =False
        for idx, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][idx] = (key,value)
                Found = True
                break
        if not Found:
                self.arr[hash].append((key,value))

    def getvalue(self,key):
        hash = self.gethash(key)
        for element in self.arr[hash]:   # to return value of a specifc key in linked list by iterating through linked list
            if(element[0] == key):
                return element[1]
    def deleteitem(self,key):
        hash = self.gethash(key)
        for idx, element in enumerate(self.arr[hash]):
            if(element[0] == key):
                del self.arr[hash][idx]
        # self.arr[hash] = None

obj = HashTable()
obj.add('march9','5 cr')
obj.add('march10','10 cr')
obj.add('march30','4 cr')
obj.add('march11','111 cr')
obj.add('march20','220 cr')
# print(obj.gethash('march11')) # same 
# print(obj.gethash('march20'))
# obj.deleteitem('march9')
# obj.deleteitem('march20')
# print(obj.getvalue('march9'))
# print(obj.getvalue('march20'))
print(obj.arr)


