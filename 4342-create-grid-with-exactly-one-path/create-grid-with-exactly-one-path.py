class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if m == 1:
            return ["." * n]
        grid = ["." * n]

        for _ in range(m - 1):
            grid.append("#" * (n - 1) + ".")

        return grid