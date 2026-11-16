class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s)>k:
            news=""
            for i in range(0,len(s),k):
                t=0
                for j in s[i:i+k]:
                    t+=int(j)
                news+=str(t)
            s=news
        return s
                

