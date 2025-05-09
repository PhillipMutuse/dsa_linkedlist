class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head 
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    def delete(self, key):
        if not self.head:
            return

        current = self.head
        prev = None

 
        while True:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
    
                    if current.next == self.head:
                        self.head = None  
                        return
                    else:
                      
                        tail = self.head
                        while tail.next != self.head:
                            tail = tail.next
                        self.head = current.next
                        tail.next = self.head
                return
            prev = current
            current = current.next
            if current == self.head:
                break

# Example
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
print("Initial list:")
cll.display()

cll.delete(2)
print("After deleting 2:")
cll.display()

cll.delete(10)
print("After deleting 1:")
cll.display()