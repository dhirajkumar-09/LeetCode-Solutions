class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1=[]
        for i in range(len(nums)):
            j=nums[i]
            nums1.append(nums[j])
        return nums1