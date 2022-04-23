import pandas as pd

import memory
import access

################################### LOGIC TO TAKE INPUT #####################################################
class cacheInput:
    LRU = "LRU"
    LFU = "LFU"
    FIFO = "FIFO"
    RAND = "RAND"

    def __init__(self, cacheSize, blockSize, Associativity, repPolicy, read_write, address):
        self.cacheSize = cacheSize
        self.blockSize = blockSize
        self.Associativity = Associativity
        self.repPolicy = repPolicy
        self.read_write = read_write
        self.address = address

cacheInput = cacheInput

# Read Trace file
file = pd.read_csv("sampleTrace.txt", sep=" ", header=None, 
                 names=["Read/Write", "Address"])

cacheInput.read_write = file.loc[:,"Read/Write"]
cacheInput.address = file.loc[:,"Address"]

# Take input
print("Input the required values")

print("Input total cache size")
cacheInput.cacheSize = int(input())

print("Input total block size")
cacheInput.blockSize = int(input())

print("Input Associativity, 0 => Fully Associative, 1 => Direct mapped, value(2^n) => set associative")
cacheInput.Associativity = int(input())

print("Input replacement policy: LRU, LFU, FIFO, RAND")
cacheInput.repPolicy = str(input())

print("\n")
#################### CALLING FUNCTIONS #######################
memory = memory.memory()
access = access.Access()


cacheByte = memory.getCacheSize(cacheInput.cacheSize)
blockByte = memory.getBlockSize(cacheInput.blockSize)
associatityString = memory.cacheType(cacheInput.Associativity)
replacementPolicy = memory.repPolicy(cacheInput.repPolicy)

totalAccess = access.Access(cacheInput.read_write)
# print(totalAccess[0])
# print(totalAccess[1])
# print(totalAccess[2])

readAccess = totalAccess[0]
writeAccess = totalAccess[1]
cacheAccess = totalAccess[2]

print(cacheByte)
print(blockByte)
print(associatityString)
print(replacementPolicy)
