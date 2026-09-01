class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}

        for pre in prerequisites:
            pre_map[pre[0]].append(pre[1])

        visiting = set()

        def dfs(crs):
            if pre_map[crs] == []:
                return True
    
            if crs in visiting:
                return False

            visiting.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            pre_map[crs] = []
            return True
        
        for crs in pre_map:
            if not dfs(crs):
                return False
        
        return True
            

            

