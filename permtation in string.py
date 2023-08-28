def checkInclusion( s1, s2):
        from collections import Counter
        c1 = Counter(s1)
        l = len(s1)
        c2 = Counter(s2[:l])
        if c1 == c2:
            return True
        for i in range(len(s2) - l):
            if c2[s2[i]] == 1:
                del c2[s2[i]]
            else:
                c2[s2[i]] -= 1
            c2[s2[i + l]] += 1
            print(c2)
            if c1 == c2:
                return True
            
        return False
s1 = "ab"
s2 = "eidbaooo"
checkInclusion(s1,s2)