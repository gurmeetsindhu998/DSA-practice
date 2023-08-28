def countSubstrings(s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        li=[]
        for i in range(len(s)):
            left = i
            right = i
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                counter+=1
                res = s[left : right + 1]
                left-=1
                right+=1
                li.append(res)
            left, right = i, i + 1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                counter +=1
                res = s[left : right + 1]
                left -=1
                right +=1
                li.append(res)
        return counter,li

print(countSubstrings("abbc"))