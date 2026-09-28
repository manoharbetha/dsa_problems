class Solution:
    def maxDepth(self, s: str) -> int:
        stk1=[]
        stk2=[]
        c=0
        for i in s:
            if i=='(':
                stk1.append(i)
            elif i==')':
                stk2.append(i)
            c=max(c,len(stk1)-len(stk2))
        return c            


        