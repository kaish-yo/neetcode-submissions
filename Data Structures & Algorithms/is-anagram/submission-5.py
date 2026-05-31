class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()

        for c in s:
            if s_map.get(c):
                s_map[c] += 1
            else:
                s_map[c] = 1
        
        for c in t:
            if t_map.get(c):
                t_map[c] += 1
            else:
                t_map[c] = 1

        if len(s_map) != len(t_map):
            return False

        for c in s_map:
            if t_map.get(c) and t_map[c] == s_map[c]:
                continue
            else:
                return False
        
        return True
            