class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        import fractions
        le=2*n+1
        lo=2*n
        se=0
        so=0
        for i in range(2,le,2):
            se+=1
        for i in range(1,lo,2):
            so+=1
        result=fractions.gcd(se,so)
        return result