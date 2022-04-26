import pandas as pd
import math

import memory
import access
import hexToBinary
import getbits
import getset
import hitmiss
import dataarray
import tagarray

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
hitmissObj = hitmiss.HitMiss
dataarrayObj = dataarray.DataArray
tagarrayObj = tagarray.TagArray

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



# converting address to binary
addrBinary = []
for item in cacheInputObj.address:
    addrBinary.append(hexToBinaryObj.hextobinary(item))



# get set
sets = int(getsetObj.getset(cacheByte, blockByte, cacheInputObj.Associativity))


# getting bits to binary
indexBits = []
tagBits = []
offsetBits = []
logsets = int(math.log(sets, 2))
for item in addrBinary:
    indexBits.append(getbitsObj.index_bits(item, cacheInputObj.blockSize, logsets))
    tagBits.append(getbitsObj.tag_bits(item, cacheInputObj.blockSize, logsets))
    offsetBits.append(getbitsObj.offset_bits(item, cacheInputObj.blockSize))


# Calling datastore and tagstore
dataStore = dataarrayObj.dataarray(sets, cacheInputObj.Associativity, cacheByte)
tagStore = tagarrayObj.tagArray(sets)
taglist = tagStore[0]
# print(type(taglist))
if(cacheInputObj.repPolicy == "FIFO"):
    (cache_miss, compulsory_miss, capacity_miss, conflict_miss, read_miss, write_miss, dirty_blocks_evicted) = hitmissObj.fifo(tagBits,cacheInputObj.read_write, indexBits, offsetBits, cacheInputObj.Associativity, sets, cacheByte, cacheInputObj.address)
else:
    (cache_miss, compulsory_miss, capacity_miss, conflict_miss, read_miss, write_miss, dirty_blocks_evicted) = hitmissObj.lru(tagBits,cacheInputObj.read_write, indexBits, offsetBits, cacheInputObj.Associativity, sets, cacheByte, cacheInputObj.address)

############################### OUTPUT ######################################3
print("\n")
print(cacheByte)
print(blockByte)
print(associatityString)
print(replacementPolicy)
print("Access data")
print("Read Access: ", readAccess)
print("Write Access: ", writeAccess)
print("Cache Access: ", cacheAccess)

print("CacheMiss = ", cache_miss)
print("CompulsoryMiss = ", compulsory_miss)
print("CapacityMiss = ", capacity_miss)
print("ConflictMiss = ", conflict_miss)
print("Read Miss = ", read_miss)
print("Write_miss = ", write_miss)
print("Dirty blocks evicted =", dirty_blocks_evicted)