class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        arr = sorted(nums)
        n=len(arr)
        l, r = (n-1)//2 , n-1
        for k in range(n):
            if k %2 == 0:
                nums[k] = arr [l]
                l-=1
            else:
                nums[k] = arr [r]
                r-=1