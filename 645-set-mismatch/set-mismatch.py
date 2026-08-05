class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_set=set(nums)
        nums_sum=sum(nums)
        set_sum=sum(nums_set)  
        r1=nums_sum-set_sum
        for i in range(1,len(nums)+1):
            if i not in nums_set:
                return [r1,i]