class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk=[]
        res=""
        for c in s:
            if c=='(':
                if stk:
                    res+="("
                    stk.append("(")
                else:
                    stk.append("(")
            else:
                if len(stk)==1:
                    stk.pop()
                else:
                    stk.pop()
                    res+=")"
        return res

                
        