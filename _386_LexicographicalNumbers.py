class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
       # All answers start with 1, so add this to the pile
        ans = [1]
       # To make sure we don't go on forever, we need a upper limit
       # Because everything we add is guaranteed to be <= n (Explained later)
       # We can use len(ans) to keep track
        while len(ans) < n:
            # Add 0 to the last answer, because it is the next element in 
            # lexical order
            new = ans[-1] * 10
            # Suppose that exceeds the n limit
            while new > n:
                # Undo
                new //= 10
                # proceed next element in lexical order by +1 instead 
                new += 1
                # If +1 makes the number carry over
                while new % 10 == 0:    
                    # Carry over, and eliminate the following 0
                    new //= 10
            # No need to check if new <= 10
            # Because there is new/=10 while new > n
            # also there is new/=10 if carry over happens
            # so there is already a guarentee
            ans.append(new)    
        return ans

class Solution:# Time Complexity O(nlgn), space complexity O(n)
    def lexicalOrder(self, n: int) -> List[int]:
        ls = [str(i) for i in range(1, n + 1)]
        ls.sort()
        return [int(num) for num in ls]