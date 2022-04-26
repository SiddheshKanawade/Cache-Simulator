from mimetypes import types_map


class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 

class DoublyLinkedList:

    def __init__(self):
        self.head = None
 
  
    def push(self, new_data):
 

        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
 
    
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
    
    def search(self, tagAddr):
        if(self.head == None):
            return [None,-1]
        temp = self.head
        pos_tagAddr_inLL = 0
        while(temp):
            if(temp.data == tagAddr):
                
                return (temp, pos_tagAddr_inLL)
            temp = temp.next
            pos_tagAddr_inLL = pos_tagAddr_inLL + 1
        
        # if not present in LL
        return [None, -1]

    # assumed that tagaddr is present
    def replaceNode(self, searchArray):
        i = 0
        # call only when element is present
        temp = self.head
        while (i < searchArray[1]):
            self.head = self.head.next
            i = i + 1
        if(self.head.prev == None):
            return
        
        x = self.head.data
        self.head.prev.next = self.head.next
        
        
        
        if (self.head.next != None):
            self.head.next.prev = self.head.prev
            self.head.next = None
        
        self.head.prev = None
        self.head = temp
        self.push(x)
        


# llist = DoublyLinkedList()

# for i in range(10):
#     llist.push(i)
# print("\n")
# print(llist.maxCapacity())
# print("Original LL")
# llist.printList()

# searhArr = llist.search(5)
# print(searhArr[1])
# llist.replaceNode(searhArr)

 
# print ("Created DLL is: ")
# llist.printList()


 
