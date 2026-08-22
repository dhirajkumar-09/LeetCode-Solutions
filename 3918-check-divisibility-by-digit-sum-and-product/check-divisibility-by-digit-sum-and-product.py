class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        product=1
        for i in str(n):
            i=int(i)
            sum+=i
            product*=i
        return n%(sum+product)==0