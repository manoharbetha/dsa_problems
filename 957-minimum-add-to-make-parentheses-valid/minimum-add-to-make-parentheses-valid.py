class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c=0
        stk=[]
        for i in range(len(s)):
            if s[i]=="(":
                stk.append("(")
            else:
                if stk:
                    stk.pop()
                else:
                    c+=1
        if stk:
            c+=len(stk)
        return c
