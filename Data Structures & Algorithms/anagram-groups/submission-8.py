class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            anagram = "".join(sorted(word))
            res[anagram].append(word)
        
        return list(res.values())