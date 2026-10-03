class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        left_sum=0
        right_sum=0
        maxi=float('-inf')
        for i in range(k):
            left_sum+=cardPoints[i]
        maxi=left_sum
        right_ind=n-1
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            right_sum+=cardPoints[right_ind]
            maxi=max(left_sum+right_sum,maxi)
            right_ind-=1
        return maxi