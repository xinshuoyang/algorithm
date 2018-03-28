#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180327
#
################################################################################

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # quick check
        if len(s) == 0:
            return []

        for i in range(len(s)):
            ifl = False
            for word in wordDict:
                if s[i] in word:
                    ifl = True
                    break
            if not ifl:
                return []

        newdict = set()
        for word in wordDict:
            if word in s:
                newdict.add(word)
        
        prev = ""
        res = []
        self.helper(prev, s, newdict, res)
        return res

    def helper(self, prev, s, wordDict, res):
        if len(s) == 0:
            res.append(prev)
        else:
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    if prev == "":
                        self.helper(s[:i], s[i:], wordDict, res)
                    else:
                        self.helper(prev + " " + s[:i], s[i:], wordDict, res)
     

if __name__ == '__main__':
    sol = Solution()
    print sol.wordBreak("lintcode", ["de", "ding", "co", "code", "lint"])
