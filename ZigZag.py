def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    
    ret = [[] for i in range(min(numRows, len(s)))]
    #ret = []
    
    curRow = 0
    goingDown = False
    
    for ss in s:
        ret[curRow].append(ss)
        if curRow == 0 or curRow == numRows - 1:
            goingDown = not goingDown
        if goingDown:
            curRow += 1
        else:
            curRow -= 1
    
    res = []
    for r in ret:
        res.append("".join(r))
    #return "".join(ret)
    return "".join(res)

if __name__ == '__main__':
    print(convert("PAYPALISHIRING", 3))