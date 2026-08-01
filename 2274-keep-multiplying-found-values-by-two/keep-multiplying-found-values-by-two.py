class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums_list=set(nums)
        while original in nums_list:
            original*=2
        return original