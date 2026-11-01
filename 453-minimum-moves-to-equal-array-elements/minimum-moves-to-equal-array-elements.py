class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=min(nums)
        s=0
        for i in range(len(nums)):
            s+=nums[i]-m
        return s        