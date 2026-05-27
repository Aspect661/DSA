class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        dup_s = (''.join(filter(str.isalnum, s))).lower()
        if dup_s == dup_s[::-1]:
            return True
        else: 
            return False