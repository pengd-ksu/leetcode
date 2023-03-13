"""
变种，重复移除所有连续的duplicates（可以是>= 2个duplicates）， 直到不能再移除。
"""

def removeDuplicates(s: str) -> str:
    stack = []
    removeLast = False

    for c in s:
        if removeLast and c != stack[-1]:
            stack.pop()
            removeLast = False
        while stack and c == stack[-1]:
            removeLast = True
            break
        else:
            stack.append(c)

    if removeLast:
        stack.pop()
    # It's possible that we didn't have a chance to remove 
    # last one

    return ''.join(stack)


s1 = "abbaca"
print(removeDuplicates(s1))

s2 = "abbbca"
print(removeDuplicates(s2))

s3 = "abbbaaccccca"#See a problem here. Relevant with the order.
print(removeDuplicates(s3))

s4 = "aaaaccccc"
print(removeDuplicates(s4))