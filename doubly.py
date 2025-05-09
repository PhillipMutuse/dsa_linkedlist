class Node:
    def _init_(self, data):
        self.data = data         
        self.prev = None         
        self.next = None         

class DoublyLinkedList:
    def _init_(self):
        self.head = None  

  
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Display from head to tail
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            last = current 
            current = current.next
        print('None')

    # Display from tail to head
    def display_backward(self):
        current = self.head
        if not current:
            print("None")
            return
        
        while current.next:
            current = current.next
       
        while current:
            print(current.data, end=' <-> ')
            current = current.prev
        print('None')

    # Inserts a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        while current:
            if current.data == key:
               
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return  
            current = current.next

# Example 
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print("Forward:")
dll.display_forward()
print("Backward:")
dll.display_backward()

dll.insert_at_beginning(4)
print("After inserting at beginning:")
dll.display_forward()

dll.delete(2)
print("After deleting 2:")
dll.display_forward()