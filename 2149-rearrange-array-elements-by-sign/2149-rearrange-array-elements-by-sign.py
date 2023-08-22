class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []
        ans = []
        j = 0
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            else: 
                pos.append(nums[i])
        result = []
        for p_num,n_num in zip(pos,neg):
                result += [p_num,n_num]
        return result
        