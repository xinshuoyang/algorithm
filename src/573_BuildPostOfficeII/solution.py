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

        postoffice = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    postoffice[i, j] = False

        dist = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dist.append(self.distsum(i, j, grid, postoffice))
                    self.postofficeini(postoffice)
        
        if max(dist) >= 0:
            sdist = max(dist)
            for dd in dist:
                if dd >= 0 and dd < sdist:
                    sdist = dd
            return sdist
        else:
            return -1

    def distsum(self, x, y, grid, postoffice):
        """
        find the sum of distances from (x, y) to all post offices
        """
        dist = 0

        m = len(grid)
        n = len(grid[0])
        
        visit = [[False for i in range(n)] for j in range(m)]

        q1 = [[x, y]]
        visit[x][y] = True

        step = 1
        while len(q1) != 0:
            q2 = []
            for i, j in q1:
                for k, l in ((i - 1, j), (i + 1, j), (i , j - 1), (i, j + 1)):
                    if k > -1 and k < m and l > -1 and l < n:
                        if grid[k][l] == 0:
                            if not visit[k][l]:
                                visit[k][l] = True
                                q2.append([k, l])
                        elif grid[k][l] == 1:
                            if not postoffice[k, l]:
                                dist += step
                                postoffice[k, l] = True
            q1 = q2
            step += 1
        
        for pp in postoffice:
            if not postoffice[pp]:
                return -1
        return dist

    def postofficeini(self, postoffice):
        """
        initialize postoffice to be False
        """
        for pp in postoffice:
            postoffice[pp] = False
        return

if __name__ == '__main__':
    s = Solution()
    grid = [[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]

    print s.shortestDistance(grid)