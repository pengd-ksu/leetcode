class SparseVector:
    def __init__(self, nums: List[int]):
        # Only keep the position with non-zero values in a dictionary.
        self.v = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.v[i] = n
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1 = self.v
        v2 = vec.v
        result = 0
        for k1 in v1:
            if k1 in v2:
                result += v1[k1] * v2[k1]
        return result

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result

class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0
        
        while p< len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

class SparseVector: # O(1) storage, but not efficient
    def __init__(self, nums: List[int]):
        self.array = nums

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result