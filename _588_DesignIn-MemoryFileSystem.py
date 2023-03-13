from collections import defaultdict
class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.content = ""

class FileSystem:
    def __init__(self):
        self.root = Node()

    def find(self, path, create = False):
        cur = self.root
        if len(path) == 1:
            return cur
        for word in path.split('/')[1:]:
            if not cur.child.get(word, None) and not create:
                return None
            cur = cur.child[word]
        return cur
        
    def ls(self, path: str) -> List[str]:
        curr = self.find(path)
        if curr.content:#file path,return file name
            return [path.split('/')[-1]]
        return sorted(curr.child.keys())

    def mkdir(self, path: str) -> None:
        self.find(path, create = True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.find(filePath, create = True)
        curr.content += content        

    def readContentFromFile(self, filePath: str) -> str:
        curr=self.find(filePath)
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)