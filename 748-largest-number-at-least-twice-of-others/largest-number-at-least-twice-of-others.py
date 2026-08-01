class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value=max(nums)
        m_idx=nums.index(max_value)
        condition=True
        for i in range(len(nums)):
            if nums[i]!=max_value and nums[i]*2>max_value:
                condition=False
        if condition:
            return m_idx
        else:
            return -1
