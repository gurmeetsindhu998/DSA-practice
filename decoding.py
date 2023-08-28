def numDecodings( s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == '0' or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        
        #base case
        dp[0] = 1
        dp[1] = 1
        n = len(s) 
        for i in range(2, n+1): # dp array traversal
            if s[i-1] >= '1' and s[i-1] <= '9':
                dp[i] = dp[i-1] # single case
            if s[i-2] == '1':
                dp[i] += dp[i-2]
            elif s[i-2] == '2' and s[i-1] >=2 and s[i-1] <= int('6'):
                dp[i] +=  dp[i-2]
        return dp[n]

s = "123"
print(numDecodings(s))