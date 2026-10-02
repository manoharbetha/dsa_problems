class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def gen(i,o,c):
            if i==2*n:
                ans.append(''.join(sol))
                return 
            if o<n:
                sol.append('(')
                gen(i+1,o+1,c)
                sol.pop()
            if o>c:
                sol.append(')')
                gen(i+1,o,c+1)
                sol.pop()
        ans=[]
        sol=[]
        gen(0,0,0)
        return ans
                
            
            

            
            