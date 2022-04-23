
################################### LOGIC TO TAKE INPUT #####################################################
class cacheInput:
    LRU = "LRU"
    LFU = "LFU"
    FIFO = "FIFO"
    RAND = "RAND"
     
    WRITE_BACK = "WB"
    WRITE_THROUGH = "WT"

    def __init__(self, sizeMem, sizeCache, sizeBlockMem, mapPolicy, repPolicy, writePolicy):
        self.sizeMem = sizeMem
        self.sizeCache = sizeCache
        self.sizeBlockMem = sizeBlockMem
        self.mapPolicy = mapPolicy
        self.repPolicy = repPolicy
        self.writePolicy = writePolicy


cacheInput = cacheInput

print("Input the required values")

print("Input total memory size")
cacheInput.sizeMem = input()

print("Input total Cache size")
cacheInput.sizeCache = input()

print("Input size of block")
cacheInput.sizeBlockMem = input()

print("Input mapping policy")
cacheInput.mapPolicy = input()

print("Input replacement policy")
cacheInput.repPolicy = input()

print("Input write policy")
cacheInput.writePolicy = input()


