class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix, i = [], '', 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestion = []
            
            def add_sugestion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)
        
        products = sorted(products)
        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugestion(p)
        
        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestion)
        return result

class TrieNode:
    def __init__(self):
        self.word = None
        self.child = defaultdict(TrieNode)

    def addWord(self, word):
        curr = self
        for c in word:
            curr = curr.child[c]
        curr.word = word

    def getWords(self, limit):
        words = []

        def dfs(curr):
            if len(words) == limit: return
            if curr.word != None:
                words.append(curr.word)
            for c in ascii_lowercase:
                if c in curr.child:
                    dfs(curr.child[c])

        dfs(self)
        return words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for product in products:
            root.addWord(product)

        ans = []
        curr = root
        for c in searchWord:
            if curr != None and c in curr.child:
                curr = curr.child[c]
                ans.append(curr.getWords(3))
            else:
                curr = None
                ans.append([])
        return ans