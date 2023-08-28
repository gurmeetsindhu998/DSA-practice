def longestConsecutive(nums):
        num_set = set(nums)
        longest_seq = 0
        for loop in num_set:
            if loop - 1 not in num_set:
                current_seq = 1
                while loop + current_seq in num_set:
                    current_seq += 1
                longest_seq = max(longest_seq, current_seq)
        return longest_seq

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))