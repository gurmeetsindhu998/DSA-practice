def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        for i in set(s):
            if s.count(i)!= t.count(i):
                return False
        return True
s = "anagram"
t = "nagaarm"
print(isAnagram(s,t))
print(set(s))