class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # Initialize arrays to store prefix and suffix products
        prefix_products = [1] * n
        suffix_products = [1] * n

        # Compute prefix products
        prefix_product = 1
        for i in range(n):
            prefix_products[i] = prefix_product
            prefix_product *= nums[i]

        # Compute suffix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            suffix_products[i] = suffix_product
            suffix_product *= nums[i]

        # Compute the final result by multiplying prefix and suffix products
        result = [prefix_products[i] * suffix_products[i] for i in range(n)]

        return result
        