#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171206
#
################################################################################
import sys

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here

        ladders = []
        self.dfs(start, end, [], dict, ladders)
       
        ll = sys.maxint
        for ladder in ladders:
            if ll > len(ladder):
                ll = len(ladder)

        shortest = []
        for ladder in ladders:
            if len(ladder) == ll:
                shortest.append(ladder)

        return shortest 

    def dfs(self, start, end, path, dict, ladders):
        if len(path) < 5:
            if self.IsTransform(start, end):
                ladders.append(path + [start, end])
            else:
                trans = self.transform(start, dict)

                for word in trans:
                    newdict = [dd for dd in dict if dd != word]
                    self.dfs(word, end, path + [start], newdict, ladders)
        
    def transform(self, word, dict):
        """
        find all transformation of word in dict
        """

        trans = []

        for dd in dict:
            if self.IsTransform(word, dd):
                trans.append(dd)
        return trans
        
    def IsTransform(self, a, b):
        """
        determine whether a is a a character trasformation of b
        """

        m = len(a)
        n = len(b)

        if m != n:
            return False

        ndiff = 0
        for i in range(m):
            if a[i] != b[i]:
                ndiff += 1

        if ndiff == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    start = "qa"
    end = "sq"
    dict = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

    print s.findLadders(start, end, dict)
