class GetSet:
    # pass sizes in total bytes
    # associativity defines the ways
    @staticmethod
    def getset(cachesize, blocksize, associativity):
        if(associativity > 0):
            sets = cachesize/(associativity*blocksize)
        else:
            sets = cachesize/blocksize
        
        return sets
