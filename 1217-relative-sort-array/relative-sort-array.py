class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in arr2:
            counts=arr1.count(i)
            ans.extend([(i)]*counts)
        remaining=[]
        for x in arr1:
            if x not in arr2:
                remaining.append(x)
        remaining.sort()
        ans.extend(remaining)
        return ans