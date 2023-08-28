def maxAreaOfIsland( grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = [0]

        def getmax(r,c,val):
            val+=1
            grid[r][c]=2
            if r-1>=0 and grid[r-1][c]=="1": #up
                val = getmax(r-1,c,val)
            if r+1<len(grid) and grid[r+1][c]=="1": #down
                val = getmax(r+1,c,val)
            if c-1>=0 and grid[r][c-1]=="1": #left
                val = getmax(r,c-1,val)
            if c+1<len(grid[0]) and grid[r][c+1]=="1":  #right
                val = getmax(r,c+1,val)
            if val > ans[0]:
                ans[0]= val
            return val

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    getmax(i,j,0)
        
        return ans[0]

# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,1,1,0,1,0,0,0,0,0,0,0,0],
#         [0,1,0,0,1,1,0,0,1,0,1,0,0],
#         [0,1,0,0,1,1,0,0,1,1,1,0,0],
#         [0,0,0,0,0,0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]
print(maxAreaOfIsland(grid))