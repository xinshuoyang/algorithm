#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171201
#
################################################################################
import sys

class Solution:
    """
    @param: grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        if n == 0:
            return 0
        
        dist = {}
        po = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i, j] = [[sys.maxint for k in range(n)] for l in range(m)]
                    self.dist(i, j, grid, dist[i, j])

                    po.append([i, j])
        
        sdist = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dd = 0
                    for k, l in po:
                        if dist[k, l][i][j] == sys.maxint:
                            dd = sys.maxint
                            break
                        else:
                            dd += dist[k, l][i][j]
                    sdist.append(dd)
        if min(sdist) == sys.maxint:
            return -1
        else:
            return min(sdist) 
       
    def dist(self, x, y, grid, dist):
        """
        find distance from (x, y) to all empty(=0) point
        """
        m = len(grid)
        n = len(grid[0])

        visit = [[False for i in range(n)] for j in range(m)]
        
        q1 = [[x, y]]

        step = 1
        while q1:
            q2 = []
            for i, j in q1:
                for k, l in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if k >= 0 and k < m and l >= 0 and l < n\
                            and not visit[k][l] and grid[k][l] == 0:
                        dist[k][l] = step
                        visit[k][l] = True
                        q2.append((k, l))

            q1 = q2
            step += 1
            
        return dist
    
if __name__ == '__main__':
    s = Solution()
    grid = [[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
    #dist = [[sys.maxint for i in range(5)] for i in range(3)]
    #print s.dist(0, 1, grid, dist)
    print s.shortestDistance(grid)
