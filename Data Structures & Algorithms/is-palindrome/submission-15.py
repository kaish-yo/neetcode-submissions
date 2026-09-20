class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = re.sub(r"[^a-zA-Z0-9]", "", s.lower())

        backward = "".join(
            [forward[i] for i in range(len(forward) - 1, -1, -1)]
        )

        print(backward)

        if forward == backward:
            return True
        
        return False    