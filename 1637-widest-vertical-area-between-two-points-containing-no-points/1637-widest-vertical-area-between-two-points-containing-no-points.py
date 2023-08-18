class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda i:i[0])
        l = len(points)
        m = points[1][0]-points[0][0]
        for i in range(2, l):
            m = max(points[i][0]-points[i-1][0], m)
        return m
         