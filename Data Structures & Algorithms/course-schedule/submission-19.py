class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        visiting = set()

        for pre in prerequisites:
            pre_map[pre[0]].append(pre[1])
        
        def has_cycle(c):
            if c in visiting:
                return True
            if pre_map[c] == None:
                return False
            
            visiting.add(c)

            for pre in pre_map[c]:
                if has_cycle(pre):
                    return True
                
            visiting.remove(c)
            pre_map[c] = None

            return False
        
        for i in pre_map:
            if has_cycle(i):
                return False

        return True
            