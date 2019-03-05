#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190220
#
################################################################################

class Solution:
    """
    @param people: a random list of people
    @return: the queue that be reconstructed
    """
    def reconstructQueue(self, people):
        # write your code here
        if not people:
            return []
        spp = sorted(people, key=lambda x:(-x[0],x[1]))
        res = []
        for pp in spp:
            res.insert(pp[1], pp)
        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
