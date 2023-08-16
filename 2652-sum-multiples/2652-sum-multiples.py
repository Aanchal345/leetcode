class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(set(list(range(3,n+1,3))+ list(range(5,n+1,5))+list(range(7,n+1,7))))
        