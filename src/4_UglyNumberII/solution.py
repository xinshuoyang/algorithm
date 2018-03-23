#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180322
#
################################################################################


class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here

        nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

        if n <= 10:
            return nums[n - 1]
        else:
            counts = 10
            
            pp = 1
            

            while counts < n:
                # find old ugly numbers that can form the next ugly number
                aa = nums[-1]

                while nums[pp] * 5 <= aa:
                    pp += 1

                imin = nums[pp] * 5

                for i in xrange(pp, counts):
                    if nums[i] * 2 > imin:
                        break

                    for j in [2, 3, 5]:
                        itemp = nums[i] * j

                        if itemp > aa and itemp < imin:
                            imin = itemp

                nums.append(imin)
                
                counts += 1
                
            return nums[-1]
        
if __name__ == '__main__':
    sol = Solution()
    print sol.nthUglyNumber(10000)
