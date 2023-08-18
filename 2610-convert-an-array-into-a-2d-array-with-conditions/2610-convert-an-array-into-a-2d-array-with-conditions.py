class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        while nums:
            temp = []
            for i in range(len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
            result.append(temp)
            for n in temp:  # Removing the elements from nums list
                nums.remove(n)

        return result
        