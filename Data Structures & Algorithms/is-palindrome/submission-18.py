class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str = new_str + c.lower()
        
        print(new_str)
        print(new_str[::-1])
        
        return True if new_str == new_str[::-1] else False