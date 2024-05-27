class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        current = self.head
        while current.next:
            current = current.next
        current.next =  new_node  

    def insert_at_pos(self, data,pos):
        i = 0
        new_node = Node(data)
        current = self.head
        previous = self.head   
        for i in range(pos):
            previous = current
            current = current.next
        new_node.next = current    
        previous.next = new_node    


    def delete_at_beginning(self): 
        new_node = self.head
        self.head = new_node.next

    def delete_at_end(self):
        current = self.head
        previous = self.head
        while  current.next != None:
            previous = current
            current = current.next
        previous.next = None

    def delete_at_pos(self,pos): 
        i = 0
        current = self.head
        previous = self.head   
        for i in range(pos):
            previous = current
            current = current.next  
        previous.next = current.next     

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(3)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_beginning(1)
    linked_list.insert_at_end(5)
    linked_list.insert_at_pos(789,2)
    linked_list.insert_at_end(899)
    linked_list.delete_at_pos(3)



    print("Linked List:")
    linked_list.display()
