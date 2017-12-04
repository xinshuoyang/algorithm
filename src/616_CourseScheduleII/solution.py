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
            for pp in prerequisites:
                taken[pp[0]] = False
           
            p = []
            
            for i in range(numCourses):
                if taken[i]:
                    p.append(i)

            if len(p) == 0:
                return []
            
            res = [] + p
            for i in p:
                res += self.bfs(numCourses, i, taken, prerequisites)
            
            if all(taken):
                return res
            else:
                return []

    def bfs(self, numCourses, i, taken, prerequisites):
        
        q = [i]
        res = []
        
        while len(q) != 0:
            cc = q.pop()

            tt = {}
            
            for pp in prerequisites:
                if not taken[pp[0]]:
                    if pp[1] == cc:
                        if tt.has_key(pp[0]):
                            tt[pp[0]] = True and tt[pp[0]]
                        else:
                            tt[pp[0]] = True
                    else:
                        if tt.has_key(pp[0]):
                            if taken[pp[1]]:
                                tt[pp[0]] = True and tt[pp[0]]
                            else:
                                tt[pp[0]] = False and tt[pp[0]]

            for i in tt:
                if tt[i]:
                    taken[i] = True
                    res.append(i)
                    q.append(i)

        return res

if __name__ == '__main__':
    s = Solution()
    print s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
