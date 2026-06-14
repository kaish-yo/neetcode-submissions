class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        r_map = {i: [] for i in range(numCourses)}

        for c, r in prerequisites:
            r_map[c].append(r)
        
        visited = [0] * numCourses # 0: unvisited, 1: visiting, 2: visited
        
        def has_cycle(c):
            if visited[c] == 1: return True
            if visited[c] == 2: return False
            
            visited[c] = 1
            for r in r_map[c]:
                if has_cycle(r): return True
            visited[c] = 2
            return False

        for c in range(numCourses):
            if has_cycle(c):
                return False
        
        return True