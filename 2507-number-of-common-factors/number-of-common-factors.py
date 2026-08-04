class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ans=[x for x in range(1,a+1) if a%x==0]
        ans1=[x for x in range(1,a+1) if b%x==0]
        common=len(set(ans) & set(ans1))
        return common