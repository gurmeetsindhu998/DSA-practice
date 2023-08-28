def maxArea( height):
        """
        :type height: List[int]
        :rtype: int
        """
        solution = 0
        l = 0
        r = len(height)-1

        while(l < r):
            h = min(height[l], height[r])
            solution = max(solution, (r-l)*h)
            while(height[l] <= h and l < r):
                l += 1
            while(height[r] <= h and l < r):
                r -= 1
        return solution

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))