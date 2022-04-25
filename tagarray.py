class TagArray:
    @staticmethod
    # ways = associativity
    def tagArray(sets, ways):
        rows, cols = (sets, ways)
        arr = [[-1 for i in range(cols)] for j in range(rows)]
        return arr

# TagArrayObj = TagArray
# sets = 8
# ways = 4
# print(TagArrayObj.tagArray(sets, ways))