class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_slide=sum(nums[:k])
        max_sum=window_slide
        for i in range(k,len(nums)):
            window_slide+=nums[i]-nums[i-k]
            max_sum=max(max_sum,window_slide)
        return max_sum/float(k)
