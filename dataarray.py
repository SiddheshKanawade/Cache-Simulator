class DataArray:
    @staticmethod
    # pass number of set and number of ways into the function
    def dataarray(number_of_set, number_of_ways, n_block):
        set_and_way=[]
        for sets in range(number_of_set):
            a=[]
            ways=[[0 for j in range(n_block)]for i in range(number_of_ways)]
            a.append(ways)
            set_and_way.append(a)
        return set_and_way

# set = 8
# ways = 2
# # a block will be of this many bits
# block = 4
# array = DataArray
# print(array.dataarray(set, ways, block))