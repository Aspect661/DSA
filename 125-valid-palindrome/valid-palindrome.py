class Solution:
    def isPalindrome(self, s: str) -> bool:

        dup_s = ("".join(filter(str.isalnum, s))).lower()

        n = len(dup_s)

        for i in range(0,n//2,1):
            if dup_s[i] != dup_s[n-1-i]:
                return False
        return True
