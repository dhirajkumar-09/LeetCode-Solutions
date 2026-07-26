class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = "".join(char.lower() for char in s if char.isalnum())
        return result==result[::-1]