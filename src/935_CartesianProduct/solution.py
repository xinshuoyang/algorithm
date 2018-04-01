#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180331
#
##################################################

class Solution:
    """
    @param setList: The input set list
    @return: the cartesian product of the set list
    """
    def getSet(self, setList):
        # Write your code here
        if len(setList) == 0:
            return [[]]
        
        prev = []
        res = []
        self.helper(prev, setList, res)
        return res

    def helper(self, prev, setList, res):
        if len(setList) == 0:
            res.append(prev)
        else:
            for i in range(len(setList[0])):
                self.helper(prev + [setList[0][i]], setList[1:], res)

if __name__ == '__main__':
    sol = Solution()
    print sol.getSet([])
