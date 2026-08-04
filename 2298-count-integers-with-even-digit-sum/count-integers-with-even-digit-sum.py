class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        for j in range(1,num+1):
            num1=str(j)
            sum=0
            for i in num1:
                sum+=int(i)
            if sum%2==0:
                count+=1
        return count