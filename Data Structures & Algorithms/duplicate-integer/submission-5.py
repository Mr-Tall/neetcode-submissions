class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list = []
        for i in nums:
            if my_list.count(i) == 0:
                my_list.append(i)
            else:
                return True

        return False