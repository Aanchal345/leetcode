class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        c=0
        for i in sentences:
            c = max(i.count(" ")+1,c)
        return c
        