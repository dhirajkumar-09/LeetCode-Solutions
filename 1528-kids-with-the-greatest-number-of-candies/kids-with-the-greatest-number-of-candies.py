class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maximum=max(candies)
        list1=[]
        for i,candy in enumerate(candies):
            if candy+extraCandies>=maximum:
                list1.append(True)
            else:
                list1.append(False)
        return list1