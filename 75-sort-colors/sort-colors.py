class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        count=Counter(nums)
        k=0
        for i in range(3):
            for _ in range(count[i]):
                nums[k]=i
                k+=1




        