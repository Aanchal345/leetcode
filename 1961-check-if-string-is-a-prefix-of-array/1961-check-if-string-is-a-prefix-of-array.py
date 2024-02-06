class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        concatenated = ''
        for word in words:
            concatenated += word
            if concatenated == s:
                return True
            elif len(concatenated)>len(s):
                return False
        return False
        
        