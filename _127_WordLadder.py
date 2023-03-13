class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        indexToLetter = collections.defaultdict(set)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        for word in wordSet:
            for i, l in enumerate(word):
                indexToLetter[i].add(l)     
        q = collections.deque()
        q.append((beginWord, 1))
        seen = set()#to help decide whether to put a word in queue; or rather if it's a new word ever seen.
        seen.add(beginWord)
        while q:
            w, s = q.popleft()
            if w == endWord:
                return s
            for i in range(len(w)):
                for j in indexToLetter[i]:
                    nw = w[:i] + j + w[i+1:]
                    if nw in wordSet and nw not in seen:
                        q.append((nw, s + 1))
                        seen.add(nw)        
        return 0