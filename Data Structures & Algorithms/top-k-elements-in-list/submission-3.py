from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        c_sorted = sorted(counts, key=counts.get, reverse=True)
        my_list = c_sorted[:k]
        
        return my_list

