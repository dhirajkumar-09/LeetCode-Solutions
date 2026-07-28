class Solution(object):
    def removeDuplicates(self, nums):
        l1 = len(nums)

        nums_sort = sorted(set(nums))
        l2 = len(nums_sort)

        total = l1 - l2
        
        nums[:]= nums_sort + ["_"] * total

        return l2