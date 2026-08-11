class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set=set(arr)
        arr_new=[x for x in range(1,4000) if x not in arr_set]
        return arr_new[k-1]