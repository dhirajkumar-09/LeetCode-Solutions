class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return 0
        else:
            return nums.index(max(nums))
        # while left<right:
        #     mid=(left+right)//2
        #     if nums[mid]==max(nums):
        #         return mid
        #     elif (nums[mid]<max(nums)):
        #         left=mid+1
        #     else:
        #         right=mid-1