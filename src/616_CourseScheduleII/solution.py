#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171204
#
################################################################################

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here

        if numCourses == 0:
            return []
        elif numCourses == 1:
            return [0]
        else:
            taken = [True for i in range(numCourses)]

            # find courses with no prerequisites
            # find edges in/out
            edges_in = {}
            edges_out = {}
            
            for i in range(numCourses):
                edges_in[i] = []
                edges_out[i] = []

            for pp in prerequisites:
                taken[pp[0]] = False
                
                edges_in[pp[0]].append(pp[1])
                edges_out[pp[1]].append(pp[0])

            p = []
            
            for i in range(numCourses):
                if taken[i]:
                    p.append(i)

            if len(p) == 0:
                return []
            
            res = [] + p
            for i in p:
                res += self.bfs(numCourses, i, taken, edges_in, edges_out)
            
            if all(taken):
                return res
            else:
                return []

    def bfs(self, numCourses, i, taken, edges_in, edges_out):
        
        q = [i]
        res = []
        
        while len(q) != 0:
            cc = q.pop()
            for ii in edges_out[cc]:
                if not taken[ii]:
                    tt = True
                    for jj in edges_in[ii]:
                        if not taken[jj]:
                            tt = False
                            break

                    if tt:
                        taken[ii] = True
                        res.append(ii)
                        q.append(ii)
                    
        return res

if __name__ == '__main__':
    s = Solution()
    print s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
