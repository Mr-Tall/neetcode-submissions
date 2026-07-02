from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq_elements = [item[0] for item in counts.most_common(k)]
        return freq_elements