import pandas as pd
from flask import Flask, redirect, url_for, request, render_template
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
    FIFO = "FIFO"

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

# # Take input
# print("Input the required values")

# print("Input total cache size")
# cacheInputObj.cacheSize = int(input())

# print("Input total block size")
# cacheInputObj.blockSize = int(input())

# print("Input Associativity 1 => Direct mapped, value(2^n) => set associative")
# cacheInputObj.Associativity = int(input())

# print("Input replacement policy: LRU, FIFO")
# cacheInputObj.repPolicy = str(input())

# print("\n")

#################### CALLING FUNCTIONS #######################
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        
        cacheInputObj.cacheSize = int(request.form['cacheSize'])
        cacheInputObj.blockSize = int(request.form['blockSize'])
        cacheInputObj.Associativity = int(request.form['associativity'])
        cacheInputObj.repPolicy = str(request.form['policy'])
        
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

        ############################# OUTPUT FILE ##########################################3
        file = open("output.txt", "w+")
        file.write("Cache Size in Bytes: " + str(cacheByte) + "\n"
                    "Block Size in Bytes: " + str(blockByte) + "\n"
                    "Associativity: " + str(associatityString) + "\n"
                    "Replacement Policy: " + str(replacementPolicy) + "\n"
                    "Access Data" + "\n"
                    "Read Access: " + str(readAccess) + "\n"
                    "Write Access: " + str(writeAccess) + "\n"
                    "Cache Access: " + str(cacheAccess) + "\n"
                    "Miss" + "\n"
                    "Compulsory Miss: " + str(compulsory_miss) + "\n"
                    "Conflict Miss: " + str(conflict_miss) + "\n"
                    "Capacity Miss: " + str(capacity_miss) + "\n"
                    "Read Miss: " + str(read_miss) + "\n"
                    "Write Miss: " + str(write_miss) + "\n"
                    "Dirty Blocks evicted: " + str(dirty_blocks_evicted) + "\n")
        file.close()

        #####################Sending the output############################
        outputList = [cacheByte, blockByte, associatityString, replacementPolicy, readAccess, writeAccess, cacheAccess, compulsory_miss, conflict_miss, capacity_miss, read_miss, write_miss, dirty_blocks_evicted]
        outputString = ["Cache Size in Bytes", "Block Size in Bytes", "Associativity", "Replacement Policy", "Read Access", "Write Access", "Cache Access", "Compulsory Miss", "Conflict Miss", "Capacity Miss", "Read Miss", "Write Miss", "Dirty Blocks evicted"]
        output = []
        for i in range(len(outputList)):
            output.append([outputString[i], outputList[i]])

        return render_template("output.html", name = output)

if __name__ == '__main__':
   app.run(debug = True)