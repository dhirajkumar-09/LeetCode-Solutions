class Solution(object):
    def maxProduct(self, n):
        digits = []

        for i in str(n):
            digits.append(int(i))

        max_value = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                max_value = max(max_value, digits[i] * digits[j])

        return max_value