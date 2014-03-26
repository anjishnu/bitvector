"""
This is an implementation of a simple bit-based class
for efficient memory utilization in Python

MOTIVATION:
The smallest addressable unit in memory is a byte - so one bool is one byte
this leads to some pretty inefficient usage in terms of bits.
I am proposing the following class for efficient bit usage
"""

import sys

class BitVector():
    byteArray = []
    def __init__(self,numbits):
        num_of_bytes = numbits/32
        if numbits%32>0:
            num_of_bytes+=1
        # We have now computed minimum number of bytes needed for 
        # representing the bit vector
        # initialize the array
        self.byteArray = [0]*num_of_bytes

    def setBit(self,position, boolean):
        bytePosition = position/32
        bitPosition  = position%32
        tmpByte = 0
        if boolean == True:
            tmpByte = 1
            tmpByte =  tmpByte<<bitPosition
            self.byteArray[bytePosition] = self.byteArray[bytePosition]|tmpByte
        if boolean == False:
            tmpByte = sys.maxint^(2**bitPosition)
            self.byteArray[bytePosition]= self.byteArray[bytePosition]&tmpByte
        
        return

    def getBit(self,position):
        bytePosition = position/32
        bitPosition  = position%32
        byteInt = self.byteArray[bytePosition]
        byteInt = byteInt>>(bitPosition)
        if byteInt%2==1:
            return True
        else:
            return False

    