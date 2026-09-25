class Solution:
    def minimumSteps(self, s: str) -> int:
        c = s.count('1')

        ind = len(s) - c
        ans = 0
        j = ind

        for i in range(len(s)):
            if s[i] == '1':
                ans += abs(i - j)
                j += 1

        return ans