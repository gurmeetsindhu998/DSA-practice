def longestCommonPrefix(strs: list[str]) -> str:

        strs.sort()
        s1, s2, res = strs[0], strs[-1], ""

        for i in range (len(s1)):
            if s1[i] == s2[i]:
                res += s1[i]
            else:
                break
        return res
strs = ["flower","flow"]
longestCommonPrefix(strs)