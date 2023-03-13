from typing import List
import functools
from pytest import mark

class Solution:
    # Don't worry about the location of the letter we'd like to keep. Only concern
    # is number of letters. Suppose we could swap the letter we'd like to keep to
    # the first place of the words. Therefore, it doesn't matter if the letter is
    # in the right place for now. We can always suppose to be able to swap it to
    # the right place in constant time later.
    # So, key points: the letter is right (no matter if it's in the right place),
    # we proceed; not right, we can insert in insert in word1: word1 vs word2[1:]
    # Delete in word1: word1[1:] vs word2, or Replace in word1: 
    # word1[1:] vs word2[1:]
    # Lastly, the base case: one the words has already get all the necessary 
    # left, which is exactly the other. We delete the unnecessaries, which is 
    # the max of either of the words.
    @functools.cache
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        elif word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            return 1 + min(self.minDistance(word1, word2[1:]), 
                self.minDistance(word1[1:], word2), 
                self.minDistance(word1[1:], word2[1:]))

class Solution:
    # Using a tuple of two words as a key, to memorize all the intermedia results
    # in a python dictionary. Will be much faster than the first one, without
    # calling help from decorator @functools.cache.
    memo = {}
    def minDistance(self, word1: str, word2: str) -> int:
        key = (word1, word2)
        if key in self.memo.keys():
            return self.memo[key]
        if not word1 or not word2:
            self.memo[key] = max(len(word1), len(word2))
        elif word1[0] == word2[0]:
            self.memo[key] = self.minDistance(word1[1:], word2[1:])
        else:
            self.memo[key] = 1 + min(self.minDistance(word1, word2[1:]), \
                self.minDistance(word1[1:], word2), \
                self.minDistance(word1[1:], word2[1:]))
        return self.memo[key]

@mark.parametrize('word1, word2, expected', [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
    ])

def test_minDistance(word1, word2, expected):
    ans = Solution.minDistance(word1, word2)
    assert ans == expected