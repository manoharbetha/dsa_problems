class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        res=0
        l=len(nums)
        m=nums[l//2]
        for i in nums:
            res+=abs(i-m)
        return res

