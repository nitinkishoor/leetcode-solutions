class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        set_nums=list(set(nums))
        lst=[]
        for i in set_nums:
            if nums.count(i)==1:
                lst.append(i)
        return lst