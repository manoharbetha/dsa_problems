class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n==0:
            return 0
        l=[0]*len(height)
        r=[0]*len(height)
        l[0]=height[0]
        r[n-1]=height[n-1]
        for i in range(1,len(height)):
            l[i]=max(height[i],l[i-1])
        for i in range(n-2,-1,-1):
            r[i]=max(height[i],r[i+1])
        ans=0
        for i in range(1,n):
            ans+=min(l[i],r[i])-height[i]
        return ans

        