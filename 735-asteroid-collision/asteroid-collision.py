class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stk=[]
        for i in range(len(arr)):
            if arr[i]<0:
                while stk and stk[-1]>0 and stk[-1]<abs(arr[i]):
                    stk.pop()
                if stk and stk[-1]>0 and stk[-1]==abs(arr[i]):
                    stk.pop()
                elif not stk or stk[-1]<0:
                    stk.append(arr[i])
            else:
                stk.append(arr[i])
        return stk
            

