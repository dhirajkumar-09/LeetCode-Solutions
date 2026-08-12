class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return 0
        # else:
        return nums.index(max(nums))
            