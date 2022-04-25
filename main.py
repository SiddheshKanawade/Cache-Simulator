import pandas as pd

import memory
import access
import hexToBinary
import getbits
import getset

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

# Defining Objects
cacheInputObj = cacheInput
memoryObj = memory.memory()
accessObj = access.Access()
hexToBinaryObj = hexToBinary.HextoBinary
getbitsObj = getbits.Getbits
getsetObj = getset.GetSet

# Read Trace file
file = pd.read_csv("sampleTrace.txt", sep=" ", header=None, 
                 names=["Read/Write", "Address"])

cacheInputObj.read_write = file.loc[:,"Read/Write"]
cacheInputObj.address = file.loc[:,"Address"]

# Take input
print("Input the required values")

print("Input total cache size")
cacheInputObj.cacheSize = int(input())

print("Input total block size")
cacheInputObj.blockSize = int(input())

print("Input Associativity, 0 => Fully Associative, 1 => Direct mapped, value(2^n) => set associative")
cacheInputObj.Associativity = int(input())

print("Input replacement policy: LRU, LFU, FIFO, RAND")
cacheInputObj.repPolicy = str(input())

print("\n")
#################### CALLING FUNCTIONS #######################



cacheByte = memoryObj.getCacheSize(cacheInputObj.cacheSize)
blockByte = memoryObj.getBlockSize(cacheInputObj.blockSize)
associatityString = memoryObj.cacheType(cacheInputObj.Associativity)
replacementPolicy = memoryObj.repPolicy(cacheInputObj.repPolicy)

totalAccess = accessObj.Access(cacheInputObj.read_write)
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

# converting address to binary
addrBinary = []
for item in cacheInputObj.address:
    addrBinary.append(hexToBinaryObj.hextobinary(item))

print(addrBinary)

# get set
sets = int(getsetObj.getset(cacheByte, blockByte, cacheInputObj.Associativity))
print("sets: ")
print(sets)

# getting bits to binary
indexBits = []
# doubt in tag bits, should it be dependent on ways? if yes then how should i implement it
tagBits = []
offsetBits = []
for item in addrBinary:
    indexBits.append(getbitsObj.index_bits(item, cacheInputObj.blockSize, sets))
    tagBits.append(getbitsObj.tag_bits(item, cacheInputObj.blockSize, sets))
    offsetBits.append(getbitsObj.offset_bits(item, cacheInputObj.blockSize))


print("\n Index bit array")
print("\n")
print(indexBits)
print("\n")
print(tagBits)
print("\n")
print(offsetBits)

# checking output
print("\n")
print(cacheInputObj.read_write)
print("\n")
print(cacheInputObj.address)