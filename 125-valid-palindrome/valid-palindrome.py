class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        dup_s = "".join([char for char in s if char.isalnum()])
        dup_s = dup_s.lower()
        if dup_s == dup_s[::-1]:
            return True
        else: 
            return False