import collections
def orangesRotting(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        queue = []
        def turnRotten(row, col):
            if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == 1:
                grid[row][col] = 2
                queue.append((row,col))
            return

        minutes = 0
        for row in range(m):
            for column in range(n):
                if grid[row][column] == 2: 
                    queue.append((row,column))
        while queue:
            temp = queue
            queue = [] # Prep for next queue iteration/ minute
            for (r,c) in temp:
                turnRotten(r+1, c)  
                turnRotten(r, c+1)  
                turnRotten(r-1, c)
                turnRotten(r, c-1)
            if queue:
                minutes += 1

        # See if any fresh oranges remain
        for row in range(m):
            for column in range(n):
                if grid[row][column] == 1:
                    return -1
        return minutes
      

grid = [[2,1,2],
        [1,0,1],
        [0,0,0]]
print(orangesRotting(grid))