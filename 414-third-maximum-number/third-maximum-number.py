class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_list=sorted(set(nums))
        if len(nums_list)>=3:
            return nums_list[-3]
        else:
            return max(nums)
