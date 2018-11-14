class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):

        while n<-1 or n>1:
            if n%2 != 0:
                return False
            else:
                n = n/2
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfTwo(1)
