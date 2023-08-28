###
def countSubstrings(s):
        n = len(s)
        answer = 0

        for i in range(2*n-1):
            left = i//2
            right = left+i%2
            a= s[left]
            b= s[right]
            while left >= 0 and right < n and s[left] == s[right]:
                answer+=1
                right +=1
                left-=1
        return answer

    

s="abc"
print(countSubstrings(s))