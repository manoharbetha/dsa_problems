class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        ans = []
        l = 0
        s = 0

        best = [float('inf')] * (n + 1)
        result = float('inf')

        for r in range(n):
            s += arr[r]

            while l <= r and s > target:
                s -= arr[l]
                l += 1

            best[r + 1] = best[r]

            if s == target:
                length = r - l + 1

                if best[l] != float('inf'):
                    result = min(result, length + best[l])

                best[r + 1] = min(best[r + 1], length)

        return -1 if result == float('inf') else result