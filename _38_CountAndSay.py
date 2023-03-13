# def countAndSay(n: int) -> str:
#     countAndSay_dict = {}
#     ans = ""
#     count = 0
#     for i in range(1, n+1):
#         if i == 1:
#             countAndSay_dict[i] = "1"
#         else:
#             pre_num = countAndSay_dict[i-1][0]
#             for num_str in countAndSay_dict[i-1]:
#                 if num_str == pre_num:
#                     count += 1
#                 else:
#                     ans = str(count) + pre_num + ans
#                     pre_num = num_str
#                     countAndSay_dict[i] = countAndSay_dict.get(i, "") + ans
#                     count = 1
#                     ans = ""
#             if num_str == countAndSay_dict[i-1][-1]:
#                 countAndSay_dict[i] = countAndSay_dict.get(i, "") + str(count) + num_str
#             count = 0
#     return countAndSay_dict[n]
def countAndSay(n: int) -> str:
    ans = '1'
    for _ in range(n-1):
        group, count, tmp = ans[0], 0, ''
        for part in ans:
            if part == group:
                count += 1
            else:
                tmp += str(count) + group
                group = part
                count = 1
        tmp += str(count) + group
        ans = tmp
    return ans

if __name__ == '__main__':
    print(countAndSay(8))