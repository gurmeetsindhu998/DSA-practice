def threeSum(nums): 
        mem = {}
        for e in nums:
            if e not in mem:
                mem[e] = 1
            else:
                mem[e] += 1

        if 0 in mem and mem[0] >= 3:
            res = [[0, 0, 0]]
        else:
            res = []

        pos = [e for e in mem if e > 0]
        neg = [e for e in mem if e < 0]

        for p in pos:
            for n in neg:
                comp = -(p + n)
                if (comp == p or comp == n) and mem[comp] < 2:
                    continue
                if comp in mem and n <= comp <= p:
                    res.append([n, comp, p])
        return res

nums = [-1,0,1,2,2,-1,-4]
print(threeSum(nums))