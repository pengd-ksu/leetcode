from itertools import product

class Solution:
    def car_product(*args, repeat=1):
        # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
        pools = [tuple(pool) for pool in args] * repeat
        print(f"pools: {pools}")
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
            print(f"result in the loop: {result}")
        print(f"result: {result}")
        for prod in result:
            yield tuple(prod)

    def letterCombinations(digits: str):
        if digits == "":
            return []
        
        # define digit-to-letters map
        dgt_to_ltrs = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z'],
        }
        
        # get product of the digits
        ds = [int(d) for d in digits]
        a = [dgt_to_ltrs[i] for i in ds]
        return [''.join(r) for r in car_product(*a)]

    def letterCombinations_2(digits: str):
        def dfs(dic, digits, path, res):
            if not digits:
                res.append(path)
                return
            for c in dic[digits[0]]:
                dfs(dic, digits[1:], path+c, res)
        
        if not digits:
            return []
        dic = {"2": "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []
        dfs(dic, digits, '', res)
        return res


    def letterCombinations_3(self, digits: str):
        if not digits:
            return []
        dic = {2: ['a', 'b', 'c'], 
               3: ['d', 'e', 'f'], 
               4: ['g', 'h', 'i'], 
               5: ['j', 'k', 'l'], 
               6: ['m', 'n', 'o'], 
               7: ['p', 'q', 'r', 's'], 
               8: ['t', 'u', 'v'], 
               9: ['w', 'x', 'y', 'z']}
        ans = []
        def dfs(path, digits):
            if not digits:
                ans.append(path)
                return
            d = int(digits[0])# The key in dic is integer!
            for l in dic[d]:
                dfs(path + l, digits[1:])
        
        dfs('', digits)
        return ans

if __name__ == '__main__':
    print(letterCombinations_2("23"))