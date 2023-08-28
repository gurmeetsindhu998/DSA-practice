import heapq
def lastStoneWeight(stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # Picking x and y stone which are heaviest 
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            
            # We don't need to do anything if x == y because we already popped x and y

            # If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
            if x != y:
                heapq.heappush(stones,y-x)

        
        if stones:
            return abs(stones[0])
        else:
            return 0 

stones = [2,7,4,1,8,8,1]
print(lastStoneWeight(stones))