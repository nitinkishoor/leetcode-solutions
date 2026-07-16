class Solution:
    def hammingWeight(self, n: int) -> int:
        nitin =0
        while n > 0:
            c= n%2
            if c ==1:
                nitin +=1
            n//=2
        return nitin


        