class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        
        for s in strings:
            key = [0]# In case there would be single letter
            if len(s) > 1:
                for i in range(len(s) - 1):
                    key.append((ord(s[i+1]) - ord(s[i]))%26)
            result[tuple(key)].append(s)# Keep the seq numbers as key
        
        return [val for val in result.values()]

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for s in strings:
            key = tuple((ord(c) - ord(s[0]))%26 for c in s)
            mp[key].append(s)
        return mp.values()

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def shift_letter(letter: str, shift: int):
            return chr((ord(letter) - shift) % 26 + ord('a'))
        
        # Create a hash value
        def get_hash(string: str):
            # Calculate the number of shifts to make the first character to be 'a'
            shift = ord(string[0])
            return ''.join(shift_letter(letter, shift) for letter in string)
        
        # Create a hash_value (hashKey) for each string and append the string
        # to the list of hash values i.e. mapHashToList["abc"] = ["abc", "bcd"]
        groups = collections.defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)
        
        # Return a list of all of the grouped strings
        return list(groups.values())

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Create a hash value
        def get_hash(string: str):
            key = []
            for a, b in zip(string, string[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return ''.join(key)
        
        # Create a hash value (hash_key) for each string and append the string
        # to the list of hash values i.e. mapHashToList["cd"] = ["acf", "gil", "xzc"]
        groups = collections.defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)
        
        # Return a list of all of the grouped strings
        return list(groups.values())