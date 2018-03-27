#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180326
#
################################################################################

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        if n < k or n == 0:
            return [[]]

        res = []
        self.helper([], 1, n, k, res)
        return res


    def helper(self, prev, m, n, k, res):
        if k == 0:
            res.append(prev)
        
        if k > 0:
            if n - m + 1 >= k:
                if n - m + 1 == k:
                    res.append(prev + [i for i in range(m, n + 1)])
                elif n - m + k > k:
                    self.helper(prev + [m], m + 1, n, k - 1, res)
                    self.helper(prev, m + 1, n, k, res)


if __name__ == '__main__':
    sol = Solution()
    print sol.combine(4, 2)
    
