def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dic={}
        for i in strs:
            temp=''.join(sorted(i))
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp]=[i]
        return dic.values()
        

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))