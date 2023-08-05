class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        return[sum(math.sqrt((x0-x1)**2 + (y0-y1)**2) <=r for x1,y1 in points) for x0,y0,r in queries]
        