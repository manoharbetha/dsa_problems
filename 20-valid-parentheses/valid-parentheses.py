class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if i=="[" or i=="(" or i=="{":
                stk.append(i)
            else:
                if not stk:
                    return False
                p=stk.pop()
                if p=="[" and i=="]":
                    continue
                elif p=="{" and i=="}":
                    continue
                elif p=="(" and i==")":
                    continue   
                else:
                    return False
        return not stk         
                       