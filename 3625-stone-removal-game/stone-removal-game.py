
class Solution:
    def canAliceWin(self, n: int) -> bool:
        x = 10
        t = True

        while n > 0:
            if n >= x:
                n -= x
                if n == 0:
                    return t
                x -= 1
                t = not t
            else:
                return not t

        return t
