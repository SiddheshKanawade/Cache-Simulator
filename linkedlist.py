# A complete working Python
# program to demonstrate all
# insertion methods
 
# A linked list node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
# Class to create a Doubly Linked List
class DoublyLinkedList:
 
    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
 
    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def push(self, new_data):
 
        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)
 
        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head
 
        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node
 
        # 5. move the head to point to the new node
        self.head = new_node
 
    # Given a node as prev_node, insert a new node after
    # the given node
    
    def pop(self):
        if(self.head == None):
            return

        if (self.head.next == None):
            self.head = None
        
        else:
            temp = self.head
            while(self.head.next.next != None):
                self.head = self.head.next
            self.head.next.prev = None
            self.head.next = None
            self.head = temp

    def maxCapacity(self):
        if(self.head == None):
            return 0

        if(self.head.next == None):
            return 1
        
        temp = self.head
        capacity = 0
        while(self.head):
            self.head = self.head.next
            capacity = capacity + 1
        self.head = temp
        return capacity

    # This function prints contents of linked list
    # starting from the given node
    def printList(self):
 
        print("\nTraversal in forward direction")
        temp = self.head
        if(self.head == None):
            print("None")
            return
        while (self.head):
            print(" {}".format(self.head.data))
            # last = self.head
            self.head = self.head.next
 
        # print("\nTraversal in reverse direction")
        # while last:
        #     print(" {}".format(last.data))
        #     last = last.prev
        self.head = temp
 
# Driver program to test above functions
 
 
# Start with empty list
llist = DoublyLinkedList()
 

# So linked list becomes 7->6->None
 

for i in range(10):
    llist.push(i)
print("\n")
print(llist.maxCapacity())
print("\n")
for i in range(10):
    llist.pop()
 

 
print ("Created DLL is: ")
llist.printList()
 
