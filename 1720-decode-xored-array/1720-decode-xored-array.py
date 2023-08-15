class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        l=[]
        l.append(first)
        for i in range(len(encoded)):
            l.append(l[i]^encoded[i]) 
        return l
        