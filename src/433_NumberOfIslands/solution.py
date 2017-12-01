#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171130
#
################################################################################
#
#   dfs version
#
class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # find all lands
        
        m = len(grid)

        if m == 0:
            return 0

        n = len(grid[0])
        
        if n == 0:
            return
        
        visit = [[False for i in xrange(n)] for j in xrange(m)]

        counts = 0
        
        for i in xrange(m):
            for j in xrange(n):
                if self.check(i, j, grid, visit):
                    self.dfs(i, j, grid, visit)
                    counts += 1
        return counts

    def dfs(self, i, j, grid, visit):
        """
        dfs visit all adjacent grids
        """
        
        rows = [-1, 1, 0, 0]
        cols = [0, 0, -1, 1]

        visit[i][j] = True

        for k in xrange(4):
            if self.check(i + rows[k], j + cols[k], grid, visit):
                self.dfs(i + rows[k], j + cols[k], grid, visit)


    def check(self, i, j, grid, visit):
        """
        check whether (i, j) is part of an island. If so, visit 
        the entire island.
        """
        m = len(grid)
        n = len(grid[0])
        
        if i >= 0 and i < m and j >= 0 and j < n and \
                grid[i][j] == 1 and visit[i][j] == False:
            return True
        return False

#
#   bfs version
#


if __name__ == "__main__":
    soln = Solution()
    land = [[1,0],[0,1]]
    print soln.numIslands(land)
