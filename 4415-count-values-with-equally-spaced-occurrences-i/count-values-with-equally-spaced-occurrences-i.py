from collections import defaultdict
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        h=defaultdict(list)
        for i in range(len(nums)):
            h[nums[i]].append(i)
        ans=0
        for i,j in h.items():
            if len(j)==3:
                if j[1]-j[0]==j[2]-j[1]:
                    ans+=1
        return ans

