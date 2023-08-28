def canJump( nums):
        n=len(nums)
        tr=n-1
        for i in range(n-2,-1,-1):
            if i+nums[i]>=tr:
                tr=i
        return tr==0

nums = [3,2,1,0,4]
print(canJump(nums))