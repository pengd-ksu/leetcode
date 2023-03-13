from typing import List

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        h = Counter(secret)
        for idx, ch in enumerate(guess):
            if ch in h:
                if ch == secret[idx]:
                    bulls += 1
                    cows -= int(h[ch] <= 0)
                else:
                    cows += int(h[ch] > 0)
                h[ch] -= 1
                
        return "{}A{}B".format(bulls, cows)