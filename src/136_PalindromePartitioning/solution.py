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
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here

        partitions = []

        self.dfs(s, [], partitions)

        return partitions

        
    def dfs(self, s, prev, partitions):
        if s == '':
            partitions.append(prev)
        elif len(s) == 1:
            partitions.append(prev + [s])
        else:
            for i in range(1, len(s) + 1):
                if self.isPalindrome(s[:i]):
                    self.dfs(s[i:], prev + [s[:i]], partitions)


    def isPalindrome(self, s):
        """
        check whether s is palindrome
        """
        if not s:
            return True
        else:
            m = len(s)

            for i in range(len(s)):
                if s[i] != s[- i - 1]:
                    return False
            return True

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome('aa')
    partitions = []
    s.dfs('abaaba', [], partitions)
    print partitions
