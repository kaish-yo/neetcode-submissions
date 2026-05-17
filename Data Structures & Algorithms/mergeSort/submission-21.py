# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        m = len(pairs) // 2

        right = self.mergeSort(pairs[:m])
        left = self.mergeSort(pairs[m:])

        return self.merge(right, left)



    def merge(self, right, left):
        result = []
        i, j = 0, 0

        while i < len(right) and j < len(left):
            if right[i].key <= left[j].key:
                result.append(right[i])
                i += 1
            else:
                result.append(left[j])
                j += 1
            
        result.extend(right[i:])
        result.extend(left[j:])

        return result
        



