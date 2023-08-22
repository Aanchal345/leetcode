class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        return[len(set(A[:i+1]).intersection(set(B[:i+1])))for i in range(len(A))]
        