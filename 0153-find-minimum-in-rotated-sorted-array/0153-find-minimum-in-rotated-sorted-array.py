class Solution:
    def findMin(self, nums: List[int]) -> int:
        c= len (nums)
        i=0
        while i<c-1:
            if nums[i] > nums[i+1]:
                return nums[i+1]
            i+=1
        return nums[0]
        