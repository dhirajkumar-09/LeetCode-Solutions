class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        max_v=0
        for j in range(1,len(nums)):
            max_value=(nums[i]-1)*(nums[j]-1)
            i+=1
        return max(max_v,max_value)