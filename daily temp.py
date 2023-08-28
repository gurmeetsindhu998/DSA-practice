def dailyTemperatures(temperatures):
        hottest = 0
        res = [0] * len(temperatures)
        for i in reversed(range(len(temperatures))):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
            else:
                days = 1
                while temperatures[days + i] <= temperatures[i]:
                    days += res[days + i]                   
                res[i] = days
        return res

temperatures = [73,74,75,71,69,72,76,73]
dailyTemperatures(temperatures)