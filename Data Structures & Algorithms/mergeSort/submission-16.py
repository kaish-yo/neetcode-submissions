class Solution:
    def mergeSort(self, pairs: list) -> list:
        if len(pairs) <= 1:
            return pairs

        m = len(pairs) // 2
        left = self.mergeSort(pairs[:m])
        right = self.mergeSort(pairs[m:])
        
        return self.merge(left, right)
        

    def merge(self, left: list, right: list) -> list:
        result = []

        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
            
        return result