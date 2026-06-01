class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_final = sorted(set(nums))

        if not nums_final:
            return 0

        current_count = 1
        longest = 1

        for i in range(len(nums_final) - 1):
            if nums_final[i + 1] == nums_final[i] + 1:
                current_count += 1
                longest = max(longest, current_count)
            else:
                current_count = 1

        return longest
            