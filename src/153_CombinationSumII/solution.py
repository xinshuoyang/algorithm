#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171205
#
################################################################################

class Solution:
    """
    @param: num: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here

        if not num:
            return []
        
        snum = sorted(num)
        
        res = []
        prev = None
        for i in range(len(snum)):
            if snum[i] <= target and snum[i] != prev:
                self.dfs(snum[i:], target, [], 0, res)
                prev = snum[i]

            if snum[i] > target:
                break
            
        return res
    
    def dfs(self, num, target, prev, psum, combs):
        """
        dfs traverse all combinations
        """

        if not num:
            return
        elif num[0] + psum == target:
            combs.append(prev + [num[0]])
        elif num[0] + psum < target:
            visit = set()
            
            for i in range(1, len(num)):
                if num[i] not in visit:
                    self.dfs(num[i:], target, prev + [num[0]], psum + num[0], combs)
                    visit.add(num[i])

if __name__ == '__main__':
    s = Solution()
    combs = []
    s.dfs(sorted([10,1,6,7,2,1,5]), 8, [], 0, combs)
    #print combs

    print s.combinationSum2([1, 1, 1, 3, 3, 3, 5, 5, 5], 10)
