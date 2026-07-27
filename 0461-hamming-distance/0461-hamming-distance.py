class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        nitin =  x^y
        v =0
        for i in range(32):
            #if (((x&(1>>1)) == 0) and ((y&(1>>1)) >= 0))  or  (((x&(1>>1)) >= 0) and ((y&(1>>1)) == 0)):
            if (nitin & 1) == 1:
                v+=1
            nitin >>=1
        return v

        





        