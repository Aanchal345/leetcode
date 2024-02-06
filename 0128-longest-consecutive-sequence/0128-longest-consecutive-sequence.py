class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        count = 1
        max_length = 1
        for i in range(1,n):
             if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    count +=1
                else: 
                    max_length = max(max_length,count)
                    count = 1
        return max(max_length,count)
                
        