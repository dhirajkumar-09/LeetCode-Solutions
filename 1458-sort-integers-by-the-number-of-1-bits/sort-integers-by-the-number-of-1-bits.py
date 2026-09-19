class Solution:
    def countBits(self, n):
        count = 0

        while n != 0:
            n = n & (n - 1)
            count += 1

        return count

    def sortByBits(self, arr):
        arr.sort(key=lambda x: (self.countBits(x), x))
        return arr