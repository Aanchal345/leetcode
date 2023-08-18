class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        return [sum(abs(i-j) for i in range(len(boxes)) if boxes[i]=="1") for j in range(len(boxes))]
        