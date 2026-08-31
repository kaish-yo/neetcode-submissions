class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # コース -> そのコースの前提コース一覧
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting = set()  # 今たどっている経路上のノード

        def dfs(crs):
            if crs in visiting:       # 経路上に戻ってきた = 閉路
                return False
            if pre_map[crs] == []:    # 前提なし = 履修できる
                return True

            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            pre_map[crs] = []         # 通り抜けられた事を記録（メモ化）
            return True

        for c in range(numCourses):   # 非連結グラフもあるので全頂点から
            if not dfs(c):
                return False
        return True