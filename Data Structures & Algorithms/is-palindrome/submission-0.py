class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s_new = s[::-1]

        if s == s_new:
            return True
        else:
            return False
