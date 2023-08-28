def minEatingSpeed(piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        import math
        l,r = 1, max(piles)
        res = r 
        while l<=r:
            mid = (l+r)//2
            ho= 0
            for p in piles:
                ho += math.ceil(p/mid)
            if ho <= h:
                res = min(res,mid)
                r= mid-1
            else:
                l = mid+1
        return res

piles = [30,11,23,4,20]#[3,6,7,11]
h = 5
print(minEatingSpeed(piles,h))
