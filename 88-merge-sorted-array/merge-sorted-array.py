class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0
        while(len(nums1)>m):
            nums1.pop()
            i+=1
        j=0
        while(len(nums2)>n):
            nums2.pop()
            j+=1
        nums1.extend(nums2)
        nums1.sort()
        return nums1