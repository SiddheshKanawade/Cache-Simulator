class Access:

    @staticmethod
    def Access(arr):
        read = 0
        write = 0
        for item in arr:
            if (item == 0):
                read += 1
            else:
                write +=1
        cache = read + write
        return [read,write, cache]
