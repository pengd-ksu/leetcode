class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [None] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prevIdx = stack.pop()
                ans[prevIdx] = i - prevIdx
            stack.append(i)
        for j in range(len(ans)):
            if ans[j] == None:
                ans[j] = 0
        return ans

    def dailyTemperatures_2(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prevIdx = stack.pop()
                ans[prevIdx] = i - prevIdx
            stack.append(i)
        return ans

    def dailyTemperatures_3(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue# Since current day is hottest, no need to compare
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
            # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer