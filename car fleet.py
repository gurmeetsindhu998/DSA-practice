def carFleet(target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        hashTable = dict()
        stack = []
        for i in range(len(position)):
            hashTable[position[i]] = speed[i]
        position = sorted(position)[::-1]
        for i in position:
          #  print(stack)
            iTimeAtTarget = float((target - i)) / float(hashTable[i])
            if(len(stack) > 0):
                if(iTimeAtTarget <= stack[-1]):
                   # print("yes")
                    continue
            stack.append(iTimeAtTarget)
        #print(stack)
        return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
carFleet(target,position, speed)