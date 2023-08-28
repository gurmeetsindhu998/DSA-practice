def minCostClimbingStairs( cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2],cost[i+3])

        return min(cost[0], cost[1],cost[2])

cost = [1,100,1,1] #[10,15,20]
minCostClimbingStairs(cost)