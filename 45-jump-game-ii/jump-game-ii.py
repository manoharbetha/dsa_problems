class Solution:
    def jump(self, nums: List[int]) -> int:
        me=0
        c=0
        e=0
        for i in range(len(nums)-1):
            if me<i:
                return 0
            if nums[i]+i>me:
                me=nums[i]+i
            if i==e:
                c+=1
                e=me
        return c