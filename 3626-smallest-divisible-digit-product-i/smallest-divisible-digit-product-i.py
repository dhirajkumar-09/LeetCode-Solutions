class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            mul=1
            for i in str(n):
                mul*=int(i)
            if mul%t==0:
                return n
            n+=1