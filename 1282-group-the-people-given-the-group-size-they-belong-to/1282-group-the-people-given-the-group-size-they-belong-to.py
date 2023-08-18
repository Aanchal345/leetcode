class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        hmap = {}
        res = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in hmap:
                lst = []
                lst.append(i)
                if groupSizes[i] == 1:
                    res.append(lst)
                    continue
                hmap[groupSizes[i]] = lst
            else:
                hmap[groupSizes[i]].append(i)
                if len(hmap[groupSizes[i]]) == groupSizes[i]:
                    res.append(hmap[groupSizes[i]])
                    hmap.pop(groupSizes[i])
        #print("res = ", res)
        return res
        