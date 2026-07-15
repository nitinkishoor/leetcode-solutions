class Solution:
    def reverseBits(self, n: int) -> int:
        a=[]
        nitin = 0
        for i in range(32):
            a.append(str(n % 2))
            n//=2
        for master in a:
            nitin = (nitin << 1) | (master =="1")
        return nitin



        