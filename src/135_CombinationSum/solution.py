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
    @param: candidates: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        
        if not candidates:
            return []
        
        nums = sorted(list(set(candidates)))
       
        res = []
        for i in range(len(nums)):
            if nums[i] <= target:
                self.dfs(nums[i:], target, [], 0, res)
            else:
                break

        return res
    
    def dfs(self, candidates, target, prev, psum, combs):
        
        if not candidates:
            return
        else:
            if candidates[0] + psum == target:
                combs.append(prev + [candidates[0]])
            elif candidates[0] + psum <= target:
                for i in range(len(candidates)):
                    if psum + candidates[0] + candidates[i] <= target:
                        self.dfs(candidates[i:], target, prev + [candidates[0]],\
                                psum + candidates[0], combs)
                    else:
                        break

if __name__ == '__main__':
    s = Solution()
    combs = []
    s.dfs([2,3,3,2,1,3,54,6,7], 23, [], 0, combs)

    print s.combinationSum([2,3,3,2,1,3,54,6,7], 10)
