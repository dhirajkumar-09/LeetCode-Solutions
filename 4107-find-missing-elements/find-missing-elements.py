class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(min(nums),max(nums)+1,1):
            if i not in nums:
                ans.append(i)
        return ans