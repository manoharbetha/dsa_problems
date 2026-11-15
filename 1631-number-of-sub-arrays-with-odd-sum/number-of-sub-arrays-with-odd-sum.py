class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = 0
        even = 1
        s = 0
        ans = 0
        mod = 10**9 + 7

        for i in arr:
            s += i

            if s % 2 == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1

        return ans % mod