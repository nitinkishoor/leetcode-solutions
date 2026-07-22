class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            c= nums[i]
            nums.pop(i)
            if  c not in nums:
                a.append(c)
            nums.insert(i,c)
        return a


        