class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Move j until it finds the separator after the length
            while s[j] != "#":
                j += 1

            # The number before # is the length of the next string
            length = int(s[i:j])

            # The actual string starts right after #
            start = j + 1
            end = start + length

            result.append(s[start:end])

            # Move i to the start of the next encoded string
            i = end

        return result
