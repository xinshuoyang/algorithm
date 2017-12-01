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
class Solution:
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here

        if n == 0:
            return False
        elif n == 1:
            return True
        elif len(edges) == 0:
            return False
        else:
            visit = [False for i in range(n)]

            q = [edges[0][0]]
            
            while len(q) != 0:
                nod = q.pop()
                visit[nod] = True
                
                for i, j in edges:
                    if nod == i:
                        if not visit[j]:
                            visit[j] = True
                            q.append(j)
                        else:
                            if j in q:
                                return False
                    elif nod == j:
                        if not visit[i]:
                            visit[i] = True
                            q.append(i)
                        else:
                            if i in q:
                                return False

            if all(visit):
                return True
            else:
                return False

if __name__ == "__main__":
    soln = Solution()
    print soln.validTree(5, [[0, 1], [1, 2], [1, 3], [1, 4]])
#
#   bug case: n = 5, edges = [[0, 1], [1, 2], [1, 3], [1, 4]]
#
