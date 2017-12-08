class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):

        if len(nums) == 0:
            return 0

        snums = sorted(nums)

        nunique = 1
        nums[0] = snums[0]

        for i in range(1, len(snums)):
            if snums[i] != nums[nunique - 1]:
                nums[nunique] = snums[i]
                nunique += 1
        return nunique


if __name__ == '__main__':

    nums = [1,3,1,4,4,2]
    s = Solution()
    print s.deduplication(nums)