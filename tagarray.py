import linkedlist


class TagArray:
    @staticmethod
    # ways = associativity
    def tagArray(sets):
        # rows, cols = (sets, ways)
        outerArr = []
        for i in range(sets):
            outerArr.append(linkedlist.DoublyLinkedList())
        # arr = [[-1 for i in range(cols)] for j in range(rows)]
        # print(outerArr)
        # outerArr[0].push(1)
        # print(outerArr[0].head.data)
        return outerArr