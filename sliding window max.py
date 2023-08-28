def maxSlidingWindow(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)-k+1):
            a=nums[i:i+k]
            res.append(max(a))
        return res
def maxSlidingWindow2(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from queue import deque
        q = deque()
        res = []
        for i in range(len(nums)):
            if i >= k and nums[i-k] == q[0]:
                q.popleft()
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            if i >= k-1:
                res.append(q[0])
        return res
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow2(nums,k))