def rob(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            return max(nums)
        
        def findHouses(nums):
            M = [0] * len(nums)
            M[0] = nums[0]
            M[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                M[i] = max(M[i-1], (M[i-2] + nums[i]))
            return max(M[-1], M[-2])
        
        return max(findHouses(nums[:-1]), findHouses(nums[1:]))
nums = [1,2,3,1]
rob(nums)
    