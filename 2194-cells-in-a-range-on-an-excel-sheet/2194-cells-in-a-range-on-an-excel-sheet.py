class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [chr(j)+str(i)for j in range(ord(s[0]),ord(s[3])+1)for i in range(int(s[1]),int(s[4])+1)]
        