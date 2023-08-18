class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        g,p,m = 0,0,0
        res = 0
        for i in range(len(garbage)-1,-1,-1):
            res += len(garbage[i])
            if g==0 and "G" in set(garbage[i]):
                g = sum(travel[:i])
            if p==0 and "P" in set(garbage[i]):
                p = sum(travel[:i])
            if m==0 and "M" in set(garbage[i]):
                m = sum(travel[:i])
        return res+g+p+m
        