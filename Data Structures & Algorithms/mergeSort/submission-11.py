class Solution:
    def mergeSort(self, pairs: list) -> list:
        if len(pairs) <= 1:
            return pairs
        
        mid = len(pairs) // 2

        right = self.mergeSort(pairs[:mid])
        left = self.mergeSort(pairs[mid:])

        return self.merge(left, right)

    def merge(self, left: list, right: list) -> list:
        results = []

        i = 0
        j = 0

        while i < len(right) and j < len(left):
            print(f"i: {i}, j: {j}")
            if right[i].key <= left[j].key:
                results.append(right[i])
                i += 1
            else:
                results.append(left[j])
                j += 1

        results.extend(right[i:])
        results.extend(left[j:])
        
        return results