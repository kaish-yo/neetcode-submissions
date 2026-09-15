class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + (f"{len(word)}#{word}")
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            anchor_postion = s.find("#", i)
            length = int(s[i:anchor_postion])
            word = s[anchor_postion + 1:][:length]
            res.append(word)
            i = anchor_postion + 1 + length

        return res
            
