class Solution:
    def findComplement(self, num: int) -> int:
        n=[]
        while num > 0:
            c = num % 2
            n.append(c)
            num //=2
        f=0
        master = 0
        for i in n:
            if i == 0 :
                master += 2**f
                
            f+=1
        return master
