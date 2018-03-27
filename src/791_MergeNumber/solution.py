#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180326
#
##################################################


class Solution:
    """
    @param numbers: the numbers
    @return: the minimum cost
    """
    def mergeNumber(self, numbers):
        # Write your code here
        import heapq
        
        heapq.heapify(numbers)

        energy = 0
        while len(numbers) > 1:
            n1 = heapq.heappop(numbers)
            n2 = heapq.heappop(numbers)
            nn = n1 + n2
            energy += nn
            heapq.heappush(numbers, nn)

        return energy

if __name__ == '__main__':
    sol = Solution()
    print sol.mergeNumber([5,7,9,1,3])
