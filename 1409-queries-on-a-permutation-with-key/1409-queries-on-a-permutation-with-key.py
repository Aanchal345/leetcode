class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        p = list(range(1, m+1))
        res = []
        for q in queries:
            index = p.index(q)
            res.append(index)
            p.pop(index)
            p.insert(0, q)
        return res
        