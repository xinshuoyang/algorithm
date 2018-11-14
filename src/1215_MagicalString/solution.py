class Solution:
    """
    @param n: an integer 
    @return: the number of '1's in the first N number in the magical string S
    """
    def magicalString(self, n):
        if n == 0:
            return 0
        else:
            s = '122'
            res = 1
            occ = 2 

            i = 3
            while i < n:

                if int(s[occ]) == 1:
                    if int(s[i-1]) == 1:
                        s += '2'
                    else:
                        s += '1'
                        res += 1
                    occ += 1
                    i += 1
                else:
                    if int(s[i-1]) == 1:
                        s += '22'
                    else:
                        s += '11'
                        res += 2
                    occ += 1
                    i += 2
            return res 

if __name__ == '__main__':
    ss = Solution()
    print ss.magicalString(6)

