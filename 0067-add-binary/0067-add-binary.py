class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d= len(a) -1
        f = len(b)-1
        carry = 0
        master=""
        while d >= 0 or f>= 0 or carry:
            if d >=0:
                carry += int(a[d])
                d-=1
            if f>=0:
                carry += int(b[f])
                f-=1
            master = str(carry % 2) + master
            carry //= 2
        return master



