def kClosest(points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        p=sorted(points,key = lambda x: x[0]**2+x[1]**2)
        return p[:k]

points = nums = [3,2,1,5,6,4]   #[[3,3],[5,-1],[-2,4]]
print(kClosest(points,2))