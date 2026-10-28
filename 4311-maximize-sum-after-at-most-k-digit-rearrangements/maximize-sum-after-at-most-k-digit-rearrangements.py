class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        gains = []
        ans = sum(nums)

        for num in nums:
            maximized = int("".join(sorted(str(num), reverse=True)))
            gains.append(maximized - num)
        gains.sort(reverse= True)
        return ans + sum(gains[:k])
