# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

class Getbits:
    # binary = binary address
    # n_block = 
    def offset_bits(binary, n_block):
        mask = (1<<n_block)-1
        binary = int(binary)
        offset = binary & mask
        return offset

    def index_bits(binary,n_block,sets):
        binary = (str(binary))[0:-n_block:1]
        binary = int(binary)
        mask = (1<<sets)-1
        index = binary & mask
        return index
    
    def tag_bits(binary,n_block,sets):
        x = n_block+sets
        binary = (str(binary))[0:-x:1]
        binary = int(binary,2)
        return binary

# getbitsObj = Getbits
# binary = "00010000000000101111110110110100"
# offset = getbitsObj.offset_bits(binary,4)
# index = getbitsObj.index_bits(binary,4,2)
# tag = getbitsObj.tag_bits(binary, 4, 2)
# print(offset)
# print(index)
# print(tag)
