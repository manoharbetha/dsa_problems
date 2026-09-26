from collections import defaultdict

class Solution:
    def evaluate(self, s: str, kn: list[list[str]]) -> str:
        d = defaultdict(str)

        for i in range(len(kn)):
            d[kn[i][0]] = kn[i][1]

        ans = ""
        i = 0

        while i < len(s):
            if s[i] != "(":
                ans += s[i]
            else:
                j = i + 1
                stk = []

                while s[j] != ")":
                    stk.append(s[j])
                    j += 1

                st = ''.join(stk)

                if d[st]:
                    ans += d[st]
                else:
                    ans += "?"

                i = j 

            i += 1

        return ans