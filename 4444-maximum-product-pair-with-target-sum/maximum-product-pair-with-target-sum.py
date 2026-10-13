class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        s=float('-inf')
        ans=[-1,-1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and nums[i]>nums[j]:
                    if nums[i]*nums[j]>s:
                        s=nums[i]*nums[j]
                        ans=[i,j]
        
        return ans


