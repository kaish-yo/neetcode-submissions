class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_length = len(s1)
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:window_length])

        if s1_count == window_count:
            return True

        for i in range(1, len(s2) - window_length + 1):
            window_count[s2[i - 1]] -= 1            
            if window_count[s2[i - 1]] <= 0:
                del window_count[s2[i - 1]]
            
            window_count[s2[i + window_length - 1]] += 1
            
            if s1_count == window_count:
                return True
        
        return False

    