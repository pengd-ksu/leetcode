class largeKey(str):
    def __lt__(x, y):
        return x + y > y + x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numsList = [str(n) for n in nums]
        numsList.sort(key=largeKey)
        largestNum = ''.join(numsList)
        return '0' if largestNum[0] == '0' else largestNum