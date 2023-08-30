class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(word[:-1]for word in sorted(s.split(), key = lambda w:w[-1]))
        