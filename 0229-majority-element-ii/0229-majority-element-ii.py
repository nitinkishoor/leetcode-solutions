class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nitin={}
        for i in nums:
            if i in nitin:
                nitin[i]+=1
            else:
                nitin[i] =1
        c= (len(nums)//3)
        ans =[]
        for i  in nitin:
            if nitin[i] > c:
                ans.append(i)

        return ans



        