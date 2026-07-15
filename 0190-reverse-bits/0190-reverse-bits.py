class Solution:
    def reverseBits(self, n: int) -> int:
        a=[]
        nitin = 0
        '''for i in range(32):
            a.append(str(n % 2))
            n//=2'''
        for i in range (32):
            nitin = (nitin << 1) | (n & 1)
            n>>=1
        return nitin



        