#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181230
#
################################################################################
import queue
class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        if len(map) == 0:
            return False
        if len(map[0]) == 0:
            return False
        if map[0][0] == 0:
            return False

        m = len(map)
        n = len(map[0])
        
        q = queue.Queue()
        q.put([0,0])

        while not q.empty():
            idx = q.get()

            if idx[0]+1 < m:
                if map[idx[0]+1][idx[1]] is 9:
                    return True
                elif map[idx[0]+1][idx[1]] is 1:
                    q.put([idx[0]+1,idx[1]])

            if idx[1]+1 < m:
                if map[idx[0]][idx[1]+1] is 9:
                    return True
                elif map[idx[0]][idx[1]+1] is 1:
                    q.put([idx[0],idx[1]+1])
        return False

if __name__ == "__main__":
    obj = Solution()
    print(obj.reachEndpoint([[1,1,1,0],[1,1,0,1],[0,1,0,9]]))

