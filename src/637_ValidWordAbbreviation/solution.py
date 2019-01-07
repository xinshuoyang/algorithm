#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190107
#
################################################################################
import re
class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        s=re.split('(\d+)',abbr)

        jj = 0
        for i in range(len(s)):
            if s[i].isdigit():
                if s[i][0] is "0":
                    return False
                jj += int(s[i])
            else:
                if word[jj:jj+len(s[i])] == s[i]:
                    jj += len(s[i])
                else:
                    return False
        if jj != len(word):
            return False
        return True


if __name__ == "__main__":
    obj = Solution()
    #print(obj.validWordAbbreviation("internationalization","i12iz4n"))
    print(obj.validWordAbbreviation("a","01"))
