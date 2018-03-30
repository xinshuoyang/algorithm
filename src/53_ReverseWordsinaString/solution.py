#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180330
#
################################################################################

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):

        #   get all words
        word = ''
        allwords = []
        for i in range(len(s)):
            if s[i] == ' ':
                if word != '':
                    allwords.append(word)
                    word = ''
            else:
                word += s[i]
        
        if word != '':
            allwords.append(word)
            
        if len(allwords) == 0:
            return ''
        if len(allwords) == 1:
            return allwords[0]

        res = allwords[-1]
        
        for i in range(len(allwords) - 2, - 1, -1):
            res += ' ' + allwords[i]
            
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.reverseWords("word")

