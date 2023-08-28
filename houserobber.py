def rob(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return nums

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n): 
            dp[i] = max(dp[i -2] + nums[i], dp[i - 1])

        return dp[n - 1]

nums = [2,7,9,3,1]#[1,2,3,1]
print(rob(nums))