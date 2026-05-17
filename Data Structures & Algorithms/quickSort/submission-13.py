# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        return self.quickSortHelper(pairs, 0, len(pairs) - 1)

    def quickSortHelper(self, arr: List[Pair], s: int, e: int):
        
        if e - s <= 0:
            return arr

        pivot = arr[e]
        pointer = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[pointer], arr[i] = arr[i], arr[pointer]
                pointer += 1
            
        arr[pointer], arr[e] = arr[e], arr[pointer]

        self.quickSortHelper(arr, s, pointer - 1)
        self.quickSortHelper(arr, pointer + 1, e)

        return arr
        