class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones=0
        c_ones=0
        for n in nums:
            if n==1:
                c_ones+=1
                max_ones=max(max_ones,c_ones)
            else:
                c_ones=0
        return max_ones
