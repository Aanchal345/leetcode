class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rectangle = rectangle
        self.ops = []
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        self.ops.append((row1,col1,row2,col2,newValue))
      
    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        for row1,col1,row2,col2,val in reversed(self.ops):
            if row >= row1 and col >= col1 and row <= row2 and col <= col2:
                return val
        return self.rectangle[row][col]
      
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)