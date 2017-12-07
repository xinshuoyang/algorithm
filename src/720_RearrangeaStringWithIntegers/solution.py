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

class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """

    def rearrange(self, string):
        # Write your code here
        
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        alphabet = ''
        nums = ''
        
        for ss in string:
            if ss in letters:
                alphabet += ss
            else:
                nums += ss

        if len(nums) == 0:
            numstring = ''
        else:
            ss = 0
            for num in nums:
                ss += int(num)
            numstring = str(ss)

        return ''.join(sorted(alphabet)) + numstring

if __name__ == '__main__':
    s = Solution()
    print s.rearrange("AC2BEW3")
