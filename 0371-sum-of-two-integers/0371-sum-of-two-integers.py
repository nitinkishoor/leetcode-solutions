class Solution:
    def getSum(self, a: int, b: int) -> int:
        a= a & 0xFFFFFFFF
        b= b & 0xFFFFFFFF
        while b:
            nitin = ((a & b) <<1) & 0xFFFFFFFF
            a= a ^ b
            b = nitin
        return a if a < 0x80000000 else (~(a^ 0xFFFFFFFF))
