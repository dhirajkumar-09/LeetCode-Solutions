class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[]
        count=0
        potions.sort()
        for i in spells:
            left=0
            right=len(potions)-1
            while left<=right:
                mid=(left+right)//2
                if potions[mid]*i>=success:
                    right=mid-1
                else:
                    left=mid+1
            count=len(potions)-left
            ans.append(count)
        return ans