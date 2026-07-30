class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_even=[x for x in nums if x%2==0]
        nums_odd=[y for y in nums if y%2 !=0]
        nums_even.extend(nums_odd)
        return nums_even