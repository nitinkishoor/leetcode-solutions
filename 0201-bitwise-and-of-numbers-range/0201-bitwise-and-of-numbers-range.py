class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return right
        if left <= 1 or right <= 1:
            return 0
        nitin =0
        b= left+1
        n = left & b
        master =0
        while left != right:
            left >>=1
            right >>=1
            master +=1
        return left << master

        while right > b:
            d = b+1 & n
            b +=1
            n = d
            if  d == 0:
                return 0
            
        return n

        