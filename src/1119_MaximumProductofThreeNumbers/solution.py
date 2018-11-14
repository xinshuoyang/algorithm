class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """
    def maximumProduct(self, nums):
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]

        neg = []
        pos = []
        nz = 0
        
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            elif nums[i] == 0:
                nz += 1
            else:
                pos.append(nums[i])

        pos = sorted(pos)
        neg = sorted(neg)
        
        np = len(pos)
        nn = len(neg)

        if np == 0:
            if nz != 0:
                return 0
            else:
                return neg[-1]*neg[-2]*neg[-3]
        elif np == 1:
            if nn >= 2:
                return pos[0]*neg[0]*neg[1]
            else:
                return 0
        elif np == 2:
            if nn > 0:
                if nz > 0:
                    return 0
                else:
                    return pos[0]*pos[1]*neg[-1]
            else:
                return 0
        else:
            if nn >= 2:
                return pos[-1]*neg[0]*neg[1]
            else:
                return pos[-1]*pos[-2]*pos[-3]

if __name__ == '__main__':
    ss = Solution()
    print ss.maximumProduct([-5,-2,1,0])
