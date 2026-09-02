class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique_number=set(nums)
        for i in nums:
            i=str(i)
            reverse_number=(int(i[::-1]))
            unique_number.add(reverse_number)
        return len(unique_number)