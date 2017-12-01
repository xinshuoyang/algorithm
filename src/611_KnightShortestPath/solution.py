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

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param: grid: a chessboard included 0 (false) and 1 (true)
    @param: source: a point
    @param: destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here

        m = len(grid)
        if m == 0:
            return -1

        n = len(grid[0])
        if n == 0:
            return -1

        if grid[destination[0]][destination[1]] == 1:
            return -1

        visit = [[False for i in range(n)] for j in range(m)]
        
        q1 = [[source[0], source[1]]]
        visit[source[0]][source[1]] = True
        
        path = 0
        
        while len(q1) != 0:
            print q1, visit
            
            q2 = []  

            for x, y in q1:
                q3 = self.nextstep(x, y, grid, visit)

                if [destination[0], destination[1]] in q3:
                    return path + 1
                else:
                    q2 += q3
            
            q1 = q2
            path += 1

        return -1
        
            
    def nextstep(self, x, y, grid, visit):
        """
        find all possible next valid step from the point (x, y) 
        """

        m = len(grid)
        n = len(grid[0])
        
        rows = [1, 1, -1, -1, 2, 2, -2, -2]
        cols = [2, -2, 2, -2, 1, -1, 1, -1]

        allsteps = []

        for i in range(8):
            if x + rows[i] >= 0 and x + rows[i] < m and\
                    y + cols[i] >= 0 and y + cols[i] < n and \
                    grid[x + rows[i]][y + cols[i]] != 1 and\
                    not visit[x + rows[i]][y + cols[i]]:
                visit[x + rows[i]][y + cols[i]] = True
                allsteps.append([x + rows[i], y + cols[i]])

        return allsteps
    
if __name__ == '__main__':
    s = Solution()
    print s.shortestPath([[0,0,0],[0,0,0],[0,0,0]], [2,0], [2,2])
