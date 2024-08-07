class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        first_Row=False
        first_Col=False

    #Check if first column has any zeroes
        for i in range(0,len(matrix)):
            if(matrix[i][0] ==0):
                first_Col = True

    # Check if first row has any zeroes
        for i in range(0,len(matrix[0])):
            if(matrix[0][i] ==0):
                first_Row = True

    #Check rest of matrix for zeros,mark the row and column using first row and column
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if(matrix[i][j] ==0):
                    matrix[0][j]=0
                    matrix[i][0]=0

    #Zerofy the marked Columns and Rows
        for i in range(1,len(matrix)):
            if(matrix[i][0]==0):
                for j in range(1,len(matrix[0])):
                    matrix[i][j]=0

        for i in range(1,len(matrix[0])):
            if(matrix[0][i]==0):
                for j in range(1,len(matrix)):
                    matrix[j][i]=0

        # Zerofy first Column and Row if necessary
        if first_Row:
            for i in range(0, len(matrix[0])):
                matrix[0][i] = 0

        if first_Col:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0

        return matrix