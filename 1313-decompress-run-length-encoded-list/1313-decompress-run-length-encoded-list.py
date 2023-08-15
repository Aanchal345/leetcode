class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return[nums[2*i+1] for i in range(len(nums)//2) for j in range(nums[2*i])]
        