class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk=[-1]
        c=0
        for i in range(len(s)):
            if s[i]=="(":
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    c=max(c,i-stk[-1])
        return c