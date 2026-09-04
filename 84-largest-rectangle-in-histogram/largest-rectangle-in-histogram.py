class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        ar=0
        stk=[]
        for i in range(len(h)):
            while stk and h[stk[-1]]>h[i]:
                ele=stk.pop()
                nse=i
                pse=-1 if not stk else stk[-1]
                ar=max(ar,h[ele]*(nse-pse-1))
            stk.append(i)
        while stk:
            ele=stk.pop()
            nse=len(h)
            pse=-1 if not stk else stk[-1]
            ar=max(ar,h[ele]*(nse-pse-1))
        return ar


