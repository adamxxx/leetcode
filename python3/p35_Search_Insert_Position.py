class Solution:
    def searchInsert(self, nums, target):
        """
        https://leetcode.com/problems/search-insert-position/description/
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for index, value in enumerate(nums):
            if target <= value:
                return index
        return len(nums)

a = Solution().searchInsert([1,3,5,6], 5)
print(a)