# HASH FUNCTION TO FIND LOCATION TO STORE VALUE
#  WE SUM UP THE ASCII OF A PARTICULAY KEY AND THEN MODULUS OF IT IS TKAEN TO FIND HASH VALUE

class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]


    def gethash(self,key):  # TO find hash of a key    ......key is mar 1 and value is 100 ( mar 1,100)
        sum = 0
        for char in key:
            sum  = sum + ord(char)   # ord used to get ascii
        return sum % self.MAX

    def add(self,key,value):    # can use set item and getitem for adding and geting value from hash
        hash = self.gethash(key)
        self.arr[hash] = value

    def getvalue(self,key):
        hash = self.gethash(key)
        return(self.arr[hash])
    def deleteitem(self,key):
        hash = self.gethash(key)
        self.arr[hash] = None

obj = HashTable()
obj.add('march9','5 cr')
obj.add('march10','10 cr')
obj.add('march30','4 cr')
obj.add('march1','3 cr')
# obj.deleteitem('march1')
# obj.deleteitem('march30')
# print(obj.getvalue('march9'))
print(obj.arr)



# class NewAdd:
#     def __init__(self,data) -> None:
#         self.data = data
    
#     def __add__(self,other):
#         sum = int (self.data) + int(other.data)
#         return NewAdd(sum)
    
# n1 =NewAdd(1)
# n2 =NewAdd('12')
# n3 = n1 + n2
# print(n3.data)

# x = 10
# x = x.__add__(5)
# print(x)
