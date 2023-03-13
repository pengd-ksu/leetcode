class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]
        t['-'] = True#Mark the end of the word

    def search(self, word: str) -> bool:
        t = self.trie
        for ch in word:
            if ch not in t:
                return False
            t = t[ch]
        return '-' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for p in prefix:
            if p not in t:
                return False
            t = t[p]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)