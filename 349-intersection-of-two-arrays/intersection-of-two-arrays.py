class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set=set(nums1)
        ans=[x for x in nums1_set if x in nums2]
        return ans
        