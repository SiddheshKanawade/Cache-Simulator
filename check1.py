# import linkedlist


# class DataArray:
#     @staticmethod
#     # pass number of set and number of ways into the function
#     def dataarray(number_of_set, number_of_ways, n_block):
#         set_and_way=[]
#         Array = [ [linkedlist.DoublyLinkedList()] * number_of_ways for i in range(number_of_set) ]
#         for sets in range(number_of_set):
#             a=[]
#             ways=[]
#             for i in range(number_of_ways):
#                 ways.append(Array[sets][i])
#             a.append(ways)
#             set_and_way.append(a)
#         return set_and_way
# DataArrayObj = DataArray
# x = DataArrayObj.dataarray(8,4,2)
# print(x)