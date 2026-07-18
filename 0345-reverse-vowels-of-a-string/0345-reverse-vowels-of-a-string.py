class Solution:
    def reverseVowels(self, s: str) -> str:
        n = "aeiouAEIOU"
        s= list(s)
        c= len(s)
        l=0
        r=c-1
        master = 0
        #master1 = 0
        nitin =""
        while l<=r:
            if l == r:
                for i in s:
                    nitin += i
                return nitin
            if s[l]  not in n:
                l+=1
            if s[r] not in n:
                r-=1

            if s[l] in n and s[r] in n:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            
        for i in s:
            nitin+=i
        return nitin
        