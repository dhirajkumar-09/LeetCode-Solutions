class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num=str(num)
        num1=int(num[::-1])
        if len(num)!=len(str(num1)):
            return False
        else:
            return True