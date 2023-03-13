from typing import List

def combinationSum2_setcheck(candidates: List[int], target: int) -> List[List[int]]:
    check_dup = set()
    def remains(cs, t, path, ret):
        if t == 0:
            if str(path) not in check_dup:
                check_dup.add(str(path))
                return ret.append(path)
        else:
            for index in range(len(cs)):
                if t < cs[index]:
                    continue
                else:
                    try:
                        remains(cs[(index+1):], t-cs[index], path+[cs[index]], ret)
                    except IndexError:
                        continue

    candidates.sort()
    ans = []
    solution = []
    remains(candidates, target, solution, ans)
    return ans

def combinationSum2_tuple(candidates: List[int], target: int) -> List[List[int]]:
    def remains(cs, t, path, ret):
        if t == 0:
            return ret.add(path)
        else:
            for index in range(len(cs)):
                if t < cs[index]:
                    continue
                else:
                    try:
                        remains(cs[(index+1):], t-cs[index], path+(cs[index],), ret)
                    except IndexError:
                        continue

    candidates.sort()
    ans = set()
    solution = tuple()
    remains(candidates, target, solution, ans)
    return ans

def combinationSum2_dp(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    dp = [None] + [set() for i in range(target)]
    for cand in candidates:
        if cand > target:
            break
        for i in range(target-cand, 0, -1):
            dp[cand+i] |= {comb + (cand,) for comb in dp[i]}

        for i in range(1, target+1):
            print(f"dp[{i}]: {dp[i]}")#testing
            
        dp[cand].add((cand,))

        print(f"dp[cand]{cand}: {dp[cand]}")#testing

    return dp[target]

if __name__ == '__main__':
    #print(combinationSum2_dp(candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], target = 27))
    #print(combinationSum2_dp(candidates = [10,1,2,7,6,1,5], target = 8))
    print(combinationSum2_dp(candidates = [2,5,2,1,2], target = 5))