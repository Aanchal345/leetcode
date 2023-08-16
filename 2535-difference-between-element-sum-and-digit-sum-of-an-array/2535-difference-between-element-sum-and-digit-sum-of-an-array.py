class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(map(lambda n: n - sum(map(int,str(n))),nums))
        