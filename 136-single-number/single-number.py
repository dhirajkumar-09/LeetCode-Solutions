class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_set=set(nums)
        m_count=0
        for i in n_set:
            if nums.count(i)==1:
                return i