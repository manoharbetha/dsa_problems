class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        s=""
        ans=0
        if num<len(str(sum)):
            return ""
        for i in range(num):
            if sum>9:
                s+="9"
                ans+=(9**2)
                sum-=9
            else:
                x=sum
                s+=str(x)
                ans+=x**2
                sum=0
        if sum:
            return ""
        return s

