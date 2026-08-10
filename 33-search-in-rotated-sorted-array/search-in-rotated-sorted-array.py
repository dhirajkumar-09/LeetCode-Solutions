class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,num in enumerate(nums):
            if target==num:
                return i
        else:
            return -1