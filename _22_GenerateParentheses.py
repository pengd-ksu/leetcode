class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = {0: [""], 1: ["()"]}
        for i in range(2, n + 1):
            if i not in ans.keys():
                ans[i] = [f"({a}){b}" for j in range(i) 
                for a in self.generateParenthesis(i-j-1) 
                for b in self.generateParenthesis(j)]
        return ans[n]