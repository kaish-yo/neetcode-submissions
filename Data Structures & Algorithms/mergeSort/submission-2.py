class Solution:
    def mergeSort(self, pairs: list) -> list:
        # ベースケース: 要素が1つ以下ならそのまま返す
        if len(pairs) <= 1:
            return pairs

        # 分割 (Divide)
        mid = len(pairs) // 2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])

        # 統合 (Merge)
        return self.merge(left, right)

    def merge(self, left: list, right: list) -> list:
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            # <= を使うことで安定ソートを保証
            if left[i].key <= right[j].key:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # 残りの要素を追加
        result.extend(left[i:])
        result.extend(right[j:])

        return result