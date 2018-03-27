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
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def minTotalDistance(self, grid):
        m = len(grid)
        n = len(grid[0])

        if m == 0 or n == 0:
            return 0

        xhomes = set()
        yhomes = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    xhomes.add(i)
                    yhomes.add(j)
        print xhomes, yhomes

        # distance in x
        xdist = 0
        for i in range(m):
            dist = 0
            for j in xhomes:
                dist += abs(i - j)

            if xdist > 
            xdist.append(dist)


        # distance in y
        ydist = []
        for i in range(n):
            dist = 0
            for j in yhomes:
                dist += abs(i - j)
            ydist.append(dist)

        print xdist, ydist
        
if __name__ == '__main__':
    sol = Solution()
    sol.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])
