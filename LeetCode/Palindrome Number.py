class Solution:
    def isPalindrome(self, x: int) -> bool:
        strg = str(x)
        revst = strg[::-1]
        if (strg == revst):
            return True
