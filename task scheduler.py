def leastInterval(tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        fLs = [0] * 26
        for t in tasks:
            idx = ord(t) - ord('A')
            fLs[idx] += 1
        
        maxf = max(fLs)
        count = [i for i in fLs if i == maxf]
        
        time = (maxf - 1) * (n + 1) + len(count)
        
        return max(time, len(tasks))

tasks = ["A","A","A","B","B","B"]
n= 2
print(leastInterval(tasks,n))