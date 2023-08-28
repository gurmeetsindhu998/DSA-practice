def characterReplacement( s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len, largest, word_dict = 0, 0, {}
        for i in range(len(s)):
            if s[i] in word_dict:
                word_dict[s[i]] += 1
            else:
                word_dict[s[i]] = 1
            if word_dict[s[i]] > largest:
                largest = word_dict[s[i]]
            if max_len - largest >= k:
                word_dict[s[i - max_len]] -= 1
            else:
                max_len += 1
        return max_len

s = "ABAB"
k = 2
print(characterReplacement(s,k))
