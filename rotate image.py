def rotate(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m= len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(i):               
                matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]

        for r in matrix:
            r.reverse()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)