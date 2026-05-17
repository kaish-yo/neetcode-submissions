from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 末尾から埋めていく（大きい方を後ろに置く）
        i = m - 1      # nums1 の有効要素の末尾
        j = n - 1      # nums2 の末尾
        k = m + n - 1   # 書き込み位置（nums1 の本当の末尾）

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # nums2 に残りがあれば先頭にコピー
        # （nums1 に残りがある場合はすでに正しい位置にいるので何もしない）
        nums1[:j + 1] = nums2[:j + 1]