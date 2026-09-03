class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                if nums[l]+nums[i]+nums[r]==0:
                    ans.append([nums[l],nums[i],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while r>l and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[i]+nums[r]<0:
                    l+=1
                else:
                    r-=1
        return ans
        
