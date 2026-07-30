class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i,num in enumerate(nums):
            nums[i]=num**2
            ans.append(nums[i])
        ans.sort()
        return ans