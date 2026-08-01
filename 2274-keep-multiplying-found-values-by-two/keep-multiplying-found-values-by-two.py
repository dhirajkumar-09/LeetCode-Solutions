class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        if original not in nums:
            return original 
        nums_list=sorted(set(nums))
        while original in nums_list:
            original*=2
        return original