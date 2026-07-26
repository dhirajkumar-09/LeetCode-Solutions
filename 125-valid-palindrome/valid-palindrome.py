class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = "".join(char.lower() for char in s if char.isalnum())
        left=0
        right=len(result)-1
        
        while left<right:
            if result[left] != result[right]:
                return False
                break
            left+=1
            right-=1
        else:
            return True