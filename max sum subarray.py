def maxSubArray( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=b=nums[0]
        for k in range(1,len(nums)):
            a=a+nums[k] if a>0 else nums[k]
            if a>b:
                b=a
        return b

nums = [-5,-4,-1]
print(maxSubArray(nums))