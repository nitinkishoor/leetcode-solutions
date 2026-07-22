class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c= len(nums)
        for i in range( 0,c,1):
            a = nums[i]
            nums.pop(i)
            if a not in nums:
                return a
            nums.insert(i,a)

            
        