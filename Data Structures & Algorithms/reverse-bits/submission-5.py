class Solution:
    def reverseBits(self, n: int) -> int:
        bits = ''
        for _ in range(32):
            if n & 1 == 1:
                bits = bits + '1'
            else:
                bits = bits + '0'
            n = n >> 1
        
        # bits += bits + ('0' * (32 - len(bits)))
        # print(bits)

        return int(bits, 2)