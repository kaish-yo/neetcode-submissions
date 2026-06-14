class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 1. 隣接リストを構築（各コースの前提科目一覧）
        prereq_map = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # 2. 各ノードの探索状態
        UNVISITED, IN_PROGRESS, COMPLETED = 0, 1, 2
        state = [UNVISITED] * numCourses

        # 3. DFS でサイクルを検出
        def has_cycle(course: int) -> bool:
            if state[course] == IN_PROGRESS:   # 探索中のノードに再到達 → サイクル！
                return True
            if state[course] == COMPLETED:     # 探索済み → 安全
                return False

            state[course] = IN_PROGRESS        # 「今まさに探索中」とマーク
            for prereq in prereq_map[course]:
                if has_cycle(prereq):
                    return True
            state[course] = COMPLETED          # 全子孫を調べ終えた → 完了
            return False

        # 4. 全コースを起点にサイクルチェック
        return not any(has_cycle(c) for c in range(numCourses))