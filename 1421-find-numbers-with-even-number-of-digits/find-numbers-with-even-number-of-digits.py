class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1=[]
        for i in nums:
            nums1.append(str(i))
        count=0
        j=0
        while j<len(nums):
            if len(nums1[j])%2==0:
                count+=1
            j+=1
        return count