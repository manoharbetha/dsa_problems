class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        e,o = 0,0
        mo= float('inf')
        for i in range(len(nums)):
            if nums[i]%2 == 0 :
                e+=1
            else:
                mo = min(mo , nums[i])
                o+=1
        if e ==0 or o == 0:
            return True
        for j in range(len(nums)):
            if nums[j]%2 == 0 and mo>=nums[j]:
                return False
        return True


    
        

        