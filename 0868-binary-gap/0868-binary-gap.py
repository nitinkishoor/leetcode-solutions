class Solution:
    def binaryGap(self, n: int) -> int:
        nitin =0
        master=0
        d=0
        for i in range(31):
            if 2**i == n:
                return 0
            c = n >> i & 1 
            if c>d:
                d=1
            if d>0:
                if n >> i & 1 :
                    nitin+=1
                    if nitin > master:
                        master = nitin
                    nitin = 0
                else:
                    nitin+=1
        return master
 