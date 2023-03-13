class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # The start procedure should stay in the stack as long as it doesn't 
        # end. Because it could always start again after kids returning. Key 
        # points: update its running time after another kid procedure starts; 
        # update its starting time once its kids finished, because it is 
        # running again.
        ans = [0] * n
        stack = [] # store beginning time and id of program
        for l in logs:
            idx, status, time = l.split(':')
            idx, time = int(idx), int(time)
            if status == 'start':
                if stack:
                    ans[stack[-1][0]] += time - stack[-1][1]
                stack.append([idx, time])
            else:
                _, start_time = stack.pop()
                ans[idx] += time - start_time + 1
                if stack:
                    stack[-1][1] = time + 1
        return ans