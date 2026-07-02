from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_string = dict(Counter(s))
        second_string = dict(Counter(t))

        if first_string == second_string:
            return True
        else:
            return False