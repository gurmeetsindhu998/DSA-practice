def setZeroes( matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))