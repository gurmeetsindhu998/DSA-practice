
from collections import Counter
def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        li= []
        for i in Counter(nums).most_common(k):
            li.append(i[0])
        return li

nums = [1,1,1,2,2,3]
topKFrequent(nums,2)