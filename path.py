def uniquePaths( m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        row = [1] * m

        for _ in range(n-1):
            new_row = [1] * m
            for i in range(m -2, -1, -1):
                new_row[i] = row[i] + new_row[i+1]
            row = new_row

        return row[0]

print(uniquePaths(3,7))