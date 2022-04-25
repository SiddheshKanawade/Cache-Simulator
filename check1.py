import linkedlist

linkedlistObj = linkedlist.DoublyLinkedList
class DataArray:
    @staticmethod
    # pass number of set and number of ways into the function
    def dataarray(number_of_set, number_of_ways, n_block):
        set_and_way=[]
        for sets in range(number_of_set):
            a=[]
            
            ways=[[0 for j in range(n_block)]for i in range(number_of_ways)]
            for i in range(number_of_ways):
                
                for j in range(number_of_ways):
                    arr = []
                    llist = linkedlist.DoublyLinkedList
                    temp = llist.head
                    for k in range(n_block):
                        temp.data = 0
                        temp.head = temp.next
                    arr[i] = llist.head

            a.append(ways)
            set_and_way.append(a)
        return set_and_way
