def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        l,u = 0,(row*col-1)
        while True:
            m = (l+u)//2
            mr = m//col
            mc = m%col
            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] > target:
                u = m-1
            else:
                l = m+1
            if l > u:
                return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
searchMatrix(matrix,30 )