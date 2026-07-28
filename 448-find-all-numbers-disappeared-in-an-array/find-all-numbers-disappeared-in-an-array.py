class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_s=(set(nums))
        list1=[]
        for num in range(1,len(nums)+1):
            if num not in nums_s:
                list1.append(num)
        return list1