def wordBreak(s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        minlen= len(wordDict[0])
        for i in wordDict:
            if minlen > len(i):
                minlen = len(i)

        for i in range(len(s)-minlen , -1, -1):
            for w in wordDict:
                a= s[i : i + len(w)]
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


s = "leetcode"
wordDict = ["leet","code"]



print(wordBreak(s,wordDict))
        