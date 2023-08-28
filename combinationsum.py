def combinationSum4(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]

        return dp[target] 

nums = [1,2,3]
target = 4
print(combinationSum4(nums,target))