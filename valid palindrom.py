def isPalindrome(s):
    chck=[]
    for i in s:
        if i.isalnum():
            chck.append(i.lower())
    #chck = "".join(chck)
    return chck == chck[::-1]





s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
