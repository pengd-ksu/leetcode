from typing import List
import collections

class Solution:
    def findLadders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        indexToLetter = collections.defaultdict(set)
        if endWord not in wordSet:
            return []
        for word in wordSet:
            for index, letter in enumerate(word):
                indexToLetter[index].add(letter)

        q = collections.deque()
        q.append((beginWord, []))
        res = []
        while q:
            word, path = q.popleft() 
            if word in wordList:
                wordList.remove(word) 
            if word == endWord:
                if not res or len(path) + 1 == len(res[0]): 
                    res.append(path + [word])
                elif len(path) + 1 > len(res[0]): 
                    break#any solution after this will be longer, so exit here.
            else:
                for i in range(len(word)):
                    for letter in indexToLetter[i]:
                        next_word = word[:i] + letter + word[i+1:]
                        if next_word in wordList:
                            q.append([next_word, path + [word]])
        return res




"""
"red"
"tax"
["ted","tex","red","tax","tad","den","rex","pee"]

deque([('red', ['red'])])
deque([('ted', ['red', 'ted']), ('rex', ['red', 'rex'])])
deque([('rex', ['red', 'rex']), ('tad', ['red', 'ted', 'tad']), ('tex', ['red', 'ted', 'tex'])])
deque([('tad', ['red', 'ted', 'tad']), ('tex', ['red', 'ted', 'tex'])])
deque([('tex', ['red', 'ted', 'tex'])])
"""