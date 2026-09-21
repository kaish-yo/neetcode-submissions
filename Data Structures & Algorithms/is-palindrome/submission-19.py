class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str = new_str + c.lower()
        
        return True if new_str == new_str[::-1] else False