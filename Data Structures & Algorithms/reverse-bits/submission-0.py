class Solution:
    def reverseBits(self, n: int) -> int:
        new_bit = ''
        for i in range(32):
            if n & 1 == 1:
                new_bit += '1'
            else:
                new_bit += '0'
            n = n >> 1
        return int(new_bit, 2)
                
        
        