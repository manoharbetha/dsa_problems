class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk=[]
        for i in range(len(s)):
            if s[i]==')':
                l=[]
                while stk[-1]!='(':
                    l.append(stk[-1])
                    stk.pop()
                
                stk.pop()
                for i in range(len(l)):
                    stk.append(l[i])
            else:
                stk.append(s[i])
        return ''.join(stk)
            