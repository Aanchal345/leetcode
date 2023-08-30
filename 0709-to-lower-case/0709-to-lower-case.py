class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join([chr(ord(char)+32)if ord(char)<=90 and ord(char)>=65 else char for char in s])
        