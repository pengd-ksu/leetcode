class Solution: # Convert back is too time consuming. Time Limit Exceeded
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        expand1, expand2 = [], []
        for enc1 in encoded1:
            expand1.extend([enc1[0]] * enc1[1])
        for enc2 in encoded2:
            expand2.extend([enc2[0]] * enc2[1])
            
        #print(expand1)
        
        product = []
        idx = 0
        while idx < len(expand1):
            product.append(expand1[idx] * expand2[idx])
            idx += 1
        result = []
        j = 1
        count = 1

        while j < len(product):
            if product[j] != product[j-1]:
                result.append([product[j-1], count])
                count = 1
                if j == len(product) - 1:
                    result.append([product[j], count])
            else:
                count += 1
                if j == len(product) - 1:
                    result.append([product[j], count])
            j += 1
        return result

class Solution:# Two pointers
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        idx1, idx2 = 0, 0
        result = []
        while idx1 < len(encoded1) and idx2 < len(encoded2):
            e1_val, e1_freq = encoded1[idx1][0], encoded1[idx1][1]
            e2_val, e2_freq = encoded2[idx2][0], encoded2[idx2][1]
            freq = min(e1_freq, e2_freq)
            
            prod_val = e1_val * e2_val
            
            encoded1[idx1][1] -= freq
            encoded2[idx2][1] -= freq
            
            if encoded1[idx1][1] == 0:
                idx1 += 1
            if encoded2[idx2][1] == 0:
                idx2 += 1
                
            if not result or result[-1][0] != prod_val:
                result.append([prod_val, freq])
            else:
                result[-1][1] += freq
                
        return result