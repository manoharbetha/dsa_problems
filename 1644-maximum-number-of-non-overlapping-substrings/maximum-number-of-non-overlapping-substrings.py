class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Build the smallest valid interval for each character
        for c in range(26):
            if first[c] == n:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                # This character occurs before l,
                # so we cannot make a valid substring starting at l.
                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                i += 1

            if valid:
                intervals.append((r, l))

        # Sort by ending position
        intervals.sort()

        result = []
        end = -1

        # Greedily choose the interval ending earliest
        for r, l in intervals:
            if l > end:
                result.append(s[l:r + 1])
                end = r

        return result