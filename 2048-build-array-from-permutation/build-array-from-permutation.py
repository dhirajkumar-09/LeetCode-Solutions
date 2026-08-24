class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[nums[nums[x]]for x in range(0,len(nums))]
        return ans