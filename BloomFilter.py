import numpy as np
import hashlib

class BloomFilter:
    bitset_1 = None
    bitset_2 = None
    size = 0

    def __init__(self, size):
        self.size = size
        self.bitset_1 = np.zeros([size],dtype=bool) 
        self.bitset_2 = np.zeros([size],dtype=bool) 


    def set_bitset(self, bitset):
        bitset = int(hashlib.sha256(bitset.encode()).hexdigest(), 16)
        bitset_1 = (bitset * 2 + 25) * 17 % self.size
        bitset_2 = (bitset + 24) * 23 % self.size

        self.bitset_1[bitset_1] = True
        self.bitset_2[bitset_2] = True

    def __contains__(self, find_value):
        find_value = int(hashlib.sha256(find_value.encode()).hexdigest(), 16)
        index = (find_value * 2 + 25) * 17 % self.size
        index_2 = (find_value + 24) * 23 % self.size

        return self.bitset_1[index] and self.bitset_2[index_2]