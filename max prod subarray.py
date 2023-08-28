def maxProduct( nums):
        res = nums[0]
        cur_min, cur_max = 1, 1

        for n in nums:
            tmp = cur_max * n
            cur_max = max(tmp, cur_min * n, n)
            cur_min = min(tmp, cur_min * n, n)
            res = max(res, cur_max)

        return res
         # O(n)/O(1) : Time/Memory
        
nums = [2,3,-2,-4,4]
print(maxProduct(nums))