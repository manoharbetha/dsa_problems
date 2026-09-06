class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        r=0
        f=[0,0,0]
        for i in range(len(s)):
            f[ord(s[i])-ord('a')]+=1
            while f[0]>0 and f[1]>0 and f[2]>0:
                r+=len(s)-i
                f[ord(s[l])-ord('a')]-=1
                l+=1
        return r
