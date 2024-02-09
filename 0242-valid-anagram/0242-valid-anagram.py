class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for x in 'abcdefghijklmnopqrstuvwxyz':
            if s.count(x)!= t.count(x):
                return False
        return True
        