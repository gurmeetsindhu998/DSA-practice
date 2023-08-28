def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1
        for i in nums2:
            nums.append(i)
        nums.sort()
        if len(nums)%2 == 1:
            return nums[len(nums)//2]
        # len(nums)/2 rounds down
        hi = int(len(nums)/2)
        li = hi - 1
        high = nums[hi]
        low = nums[li]
        return float(high + low)/2

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1,nums2))