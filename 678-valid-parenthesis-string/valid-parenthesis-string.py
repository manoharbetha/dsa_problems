class Solution:
    def checkValidString(self, s: str) -> bool:
        l,r,c=0,0,0
        for i in range(len(s)):
            if s[i]=='(':
                l+=1
            elif s[i]==')':
                r+=1
            else:
                c+=1
            if l+c<r:
                return False
        l,r,c=0,0,0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='(':
                l+=1
            elif s[i]==')':
                r+=1
            else:
                c+=1
            if l>c+r:
                return False
                
        return True