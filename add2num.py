def twoSum(nums: list[int], target: int) -> list[int]:
        prevMap = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))


def twoSum2(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t in d:
                return[d[t]+1,i+1]
            else:
                d[numbers[i]] = i 

print(twoSum2(nums,target))