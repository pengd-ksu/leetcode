def isMatch_recursive(s: str, p: str) -> bool:
    if not p:
        return not s
    
    if p[0] == '*':
        if not s:
            for item in p:
                if item != '*':
                    return False
            return True
        else:
            return isMatch_recursive(s[1:], p) or isMatch_recursive(s, p[1:])
    else:
        if not s:
            return False
        return (bool(s[0]) and p[0] in {s[0], '?'}) and isMatch_recursive(s[1:], p[1:])

def isMatch_dp(s: str, p: str) -> bool:
    #one more in 2d list to represent when both are empty, which is denoted by dp[0][0]
    #dp[i] corresponds to s[i-1] and p[j-1]
    dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]#default is false
    dp[0][0] = True#both empty, match
    k = 1
    while k < len(p) + 1 and p[k - 1] == '*':
        dp[0][k] = True#when s is empty and p not, it only matches when p contains all *
        k += 1
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j-1]
                #dp[i-1][j] corresponds to s[i-2] and p[j-1], since * matches any, one
                #more to string s[i-2] (which will be s[i-1]) will still match p[j-1]

                #dp[i][j-1] corresponds to s[i-1] and p[j-2], since s[i-1] already
                #matches p[j-2], one more * will correspond to empty and still matches
                #s[i-1] and p[j-1] 
            else:
                dp[i][j] = ((s[i-1] == p[j-1]) or (p[j-1] == '?')) and dp[i-1][j-1]
    return dp[len(s)][len(p)]

if __name__ == '__main__':
    print(isMatch_dp(s="aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab", 
        p="*ab***ba**b*b*aaab*b"))