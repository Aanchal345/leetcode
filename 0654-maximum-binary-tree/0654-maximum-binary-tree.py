# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:  return
        max_pair = max([(num, idx) for idx, num in enumerate(nums)]) # [maxNum's value, maxNums's idx]
        return TreeNode(max_pair[0],
                        self.constructMaximumBinaryTree(nums[: max_pair[1]]), # left children: just sub-problem
                        self.constructMaximumBinaryTree(nums[max_pair[1] + 1 :])) # right children: just sub-problem

        