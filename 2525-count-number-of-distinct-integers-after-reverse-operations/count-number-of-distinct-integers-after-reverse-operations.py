class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique_number=set(nums)
        ans=[]
        for i in nums:
            i=str(i)
            ans.append(int(i[::-1]))
        for num in ans:
            unique_number.add(num)
        return len(unique_number)