import linkedlist

class DataArray:
    @staticmethod
    # pass number of set and number of ways into the function
    def dataarray(number_of_set, number_of_ways, n_block):
        outerArr=[]
        innerArr = [0]*(n_block)
        for sets in range(number_of_set):
            datallist = linkedlist.DoublyLinkedList()
            for ways in range(number_of_ways):
                datallist.push(innerArr)
            outerArr.append(datallist)
        return outerArr

# set = 8
# ways = 2
# # a block will be of this many bits
# block = 4
# outerArray = DataArray
# arr = outerArray.dataarray(set, ways, block)

# for item in arr:
#     item.printList()
