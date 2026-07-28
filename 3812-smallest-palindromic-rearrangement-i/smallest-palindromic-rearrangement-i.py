class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        half_len=n//2
        left_half = sorted(list(s[:half_len]))
        left_str = "".join(left_half)
        mid_str = s[half_len] if n % 2 != 0 else ""
        return left_str + mid_str + left_str[::-1]