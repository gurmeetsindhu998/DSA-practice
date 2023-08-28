def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        curr_str = ""
        for char in s:
            idx = curr_str.find(char)
            curr_str += char
            if idx != -1:
                max_len = max(max_len, len(curr_str) - 1)
                curr_str = curr_str[idx + 1:]
        max_len = max(max_len, len(curr_str))
        return max_len
lengthOfLongestSubstring(s = "abcabcbb")