class Solution:
    def reverseDegree(self, s: str) -> int:
        m=1
        for i in range(len(s)):
            m+=(i+1)*(26-(ord(s[i])-ord('a')))
        return m-1