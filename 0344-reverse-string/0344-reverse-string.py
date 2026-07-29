class Solution:
    def reverseString(self, s: List[str]) -> None:
        c= len(s)
        for i in range(c//2): 
            s[i],s[c-1] = s[c-1],s[i]
            c-=1
        """
        Do not return anything, modify s in-place instead.
        """
        