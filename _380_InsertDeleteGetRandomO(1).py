class RandomizedSet:

    def __init__(self):
        self.ls = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            idx = len(self.ls)
            self.dic[val] = idx
            self.ls.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            idx = self.dic[val]
            last = self.ls[-1]
            lastIdx = self.dic[last]
            self.ls[idx], self.ls[lastIdx] = self.ls[lastIdx], self.ls[idx]
            self.dic[last] = idx
            self.ls.pop()
            del self.dic[val]
            return True
        else:
            return False
    def getRandom(self) -> int:
        import random
        r = random.randint(0, len(self.ls) - 1)
        return self.ls[r]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


from random import choice
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already 
        contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the 
        specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)