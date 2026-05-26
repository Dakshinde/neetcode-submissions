class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list = []
        for num in nums:
            if num in my_list:
                return True
            else:
                my_list.append(num)
        return False
