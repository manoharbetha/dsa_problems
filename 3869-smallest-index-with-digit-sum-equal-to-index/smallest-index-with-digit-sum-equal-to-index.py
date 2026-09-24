class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=nums[i]
            su=0
            while s>0:
                su+=(s%10)
                s=s//10
            if i==su:
                return i
        return -1
