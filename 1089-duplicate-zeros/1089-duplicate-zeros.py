class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        c= len (arr)
        i=0
        while i<c:
            if arr[i]==0:
                arr.insert(i+1,0)
                i+=2
                arr.pop(-1)
            else:
                i+=1
        return arr   