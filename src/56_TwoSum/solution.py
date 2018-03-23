#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180323
#
##################################################



class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here

        snums = sorted(numbers)
        index = sorted(range(len(numbers)), key=lambda k: numbers[k])

        for i in xrange(len(snums)):

            first = i + 1
            last = len(snums) - 1

            while first + 1 < last:
                mid = first + (last - first) / 2
                
                if snums[i] + snums[mid] == target:
                    index1, index2 = index[i], index[mid] 

                    if index1 < index2:
                        return index1, index2
                    else:
                        return index2, index1

                elif snums[i] + snums[mid] >= target:
                    last = mid
                else:
                    first = mid

            if snums[i] + snums[first] == target:
                index1, index2 = index[i], index[first]

                if index1 < index2:
                    return index1, index2
                else:
                    return index2, index1

            elif snums[i] + snums[last] == target:
                index1, index2 = index[i], index[last]

                if index1 < index2:
                    return index1, index2
                else:
                    return index2, index1

if __name__ == '__main__':
    sol = Solution()
    print sol.twoSum([0, 4, 3, 0], 0)
