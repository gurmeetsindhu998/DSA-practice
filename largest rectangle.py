def largestRectangleArea( heights):
        calc_area = lambda l, r, h: (r - l + 1) * h

        n = len(heights)
        if n == 1:
            return heights[0]
            
        max_area = 0

        stack = [0]
        for i in range(1, n):
            h = heights[i]
            if h > heights[stack[-1]]:
                stack.append(i)

            elif h < heights[stack[-1]]:
                while stack and h < heights[stack[-1]]:
                    j = stack.pop(-1)
                    max_area = max(max_area, calc_area(j, i-1, heights[j]))

                heights[j] = heights[i]
                stack.append(j)

        max_area = max(max_area, max((calc_area(i, n-1, heights[i]) for i in stack)))

        return max_area

heights = [2,1,5,6,2,3]
largestRectangleArea(heights)