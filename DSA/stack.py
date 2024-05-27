class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
        else:
            raise IndexError("pop from an empty stack")
        
    # def is_empty(self):
    #     return len(self.items) == 0

inst1 = stack()
inst1.push(100)        
inst1.push(200)        
inst1.push(300)
inst1.push(500)
inst1.push(600)
inst1.push(700)
inst1.pop()
print(inst1.items)        
