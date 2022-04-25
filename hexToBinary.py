import math

class HextoBinary:

    def hextobinary(hexstring):

        print ("Initial string", hexstring)

        # Code to convert hex to binary
        res = "{0:032b}".format(int(hexstring, 16))

        return str(res)

# obj = HextoBinary
# string = str(input())
# res = obj.hextobinary(string)
# # Print the resultant string
# print ("Resultant string", str(res))