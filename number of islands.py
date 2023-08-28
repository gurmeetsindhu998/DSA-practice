def numIslands( grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i,j):
            rows, columns = len(grid), len(grid[0]) 
            grid[i][j] = 0
            if i > 0 and grid[i-1][j]=="1":   #up
                dfs(grid, i-1, j)
            
            if i+1 < rows and grid[i+1][j]=="1":    #down
                dfs(grid, i+1, j)
            
            if j > 0 and grid[i][j-1]=="1":     #left
                dfs(grid, i, j-1)
            
            if j+1 < columns and grid[i][j+1]=="1":   #right
                dfs(grid, i, j+1)
            
            
        rows,columns,res = len(grid), len(grid[0]), 0
    
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    res += 1
                    dfs(grid, i,j)
        return res

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]

numIslands(grid)