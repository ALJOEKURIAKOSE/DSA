class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtEnd(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def insertAtPos(self,data,pos):
        new_node = Node(data)
        current = self.head
        for i in range(pos-1):
            current = current.next
        current.prev.next = new_node
        new_node.prev = current.prev
        new_node.next = current
        current.prev = new_node    

    def display(self):
        current = self.head
        while current != None:
            print(current.data ,end="<->")
            current = current.next
        print("None")    



dLL = doublyLinkedList()
dLL.insertAtBeginning(5)
dLL.insertAtBeginning(6)
dLL.insertAtBeginning(898)
dLL.insertAtBeginning(78)
dLL.insertAtBeginning(34)
dLL.insertAtEnd(1000)
dLL.insertAtPos(999,3)
dLL.display()