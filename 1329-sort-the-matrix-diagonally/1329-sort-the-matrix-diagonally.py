class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        for k in range(len(mat)-1):
            for i in range(len(mat)-1-k):
                for j in range(len(mat[0])-1):
                    if mat[i][j]>mat[i+1][j+1]:
                        mat[i][j],mat[i+1][j+1]=mat[i+1][j+1],mat[i][j]
        
                
        return mat
        