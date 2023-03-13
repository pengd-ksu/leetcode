def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    y = 0
    if x < 0:
        sign = -1
        x = -x
    else:
        sign = 1
        
    while x > 0:
        y = x % 10 + y * 10
        x = x // 10
        
    y = sign * y
    return y

if __name__ == '__main__':
    print(reverse(-10000321))