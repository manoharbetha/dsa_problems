class Solution:
    def countCommas(self, n: int) -> int:
        s=str(n)
        if len(s)<=3:
            return 0
        else:
            return n-1000+1
    