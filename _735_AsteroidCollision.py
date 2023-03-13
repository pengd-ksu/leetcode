class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            while stack and n < 0 < stack[-1]:
                if stack[-1] == -n:
                    stack.pop()
                    break
                elif stack[-1] < -n:
                    stack.pop()
                    continue
                else:
                    break
            else: # else will only be executed when while is False from the beginning
                stack.append(n)
        return stack

# This is a concise version of the code above
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            while stack and n < 0 < stack[-1]:
                if stack[-1] == -n:
                    stack.pop()
                elif stack[-1] < -n:
                    stack.pop()
                    continue
                break
            else:
                stack.append(n)
        return stack
