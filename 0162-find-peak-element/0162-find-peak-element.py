class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = nums[0]
        for i in range(len(nums)):
            if nums[i] > n:
                n = nums[i]
        for i in range(len(nums)):
            if nums[i] == n:
                return i
        