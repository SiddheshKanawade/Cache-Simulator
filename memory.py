
class memory:

    @staticmethod
    def getCacheSize(cacheSize):
        return 2**(cacheSize)

    @staticmethod
    def getBlockSize(blockSize):
        return 2**(blockSize)
    
    @staticmethod
    def cacheType(associativity):
        if(associativity == 0):
            return "Fully Associativity"
        
        elif(associativity == 1):
            return "Direct Mapped"
        
        else:
            return "Set Associativity"
    
    @staticmethod
    def repPolicy(repPol):
        return repPol