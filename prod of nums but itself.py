
def productExceptSelf(nums):
        """
        ##nice
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1,2,6,24  6.1,    4.2,   4.3.1  
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]
        
        return output


nums = [2,3,4]
print(productExceptSelf(nums))