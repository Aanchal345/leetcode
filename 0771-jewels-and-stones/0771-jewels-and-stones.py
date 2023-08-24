class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        st=Counter(stones)
        return sum([st[j]for j in jewels if j in st])
        