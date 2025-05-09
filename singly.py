class Node:
    def _init_(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node


class SinglyLinkedList:
    def _init_(self):
        self.head = None 

    # Adding a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
            return
        last = self.head
        while last.next:  
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    # Insert 
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete 
    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            return 

        prev.next = current.next
        current = None

# Example 
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()

ll.insert_at_beginning(4)
ll.display()

ll.delete(2)
ll.display()