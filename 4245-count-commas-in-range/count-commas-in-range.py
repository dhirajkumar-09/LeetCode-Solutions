class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n))<=3:
            return 0
        else:
            return (n+1)-1000