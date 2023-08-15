class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [abs(sum(nums[:n]) - sum(nums[n+1:])) for n, i in enumerate(nums)]
        