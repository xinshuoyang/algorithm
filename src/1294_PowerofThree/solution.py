class Solution:
    """
    @param n: an integer
    @return: if n is a power of three
    """
    def isPowerOfThree(self, n):
        while n<-1 or n>1:
            if n%3 != 0:
                return False
            else:
                n = n/3
        return True
