#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190112
#
################################################################################

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
#    def topk(self, nums, k):
#        # heapifiy array
#        n = len(nums)
#        for i in range(n//2-1,-1,-1):
#            self.max_heapify(nums,i,n)
#        print(nums)
#        # get the k largest numbers
#        res = []
#        for i in range(min(n,k)):
#            res.append(nums[0])
#            nums[0] = nums[n-1-i]
#            self.max_heapify(nums,0,n-1-i)
#        return res
    def max_heapify(self,nums,i,n):
        if 2*i+1 == n-1:
            if nums[i] < nums[2*i+1]:
                tmp = nums[i]
                nums[i] = nums[2*i+1]
                nums[2*i+1] = tmp
                self.max_heapify(nums,2*i+1,n)
        elif 2*i+2 < n:
            if nums[2*i+1] <= nums[2*i+2]:
                if nums[i] < nums[2*i+2]:
                    tmp = nums[i]
                    nums[i] = nums[2*i+2]
                    nums[2*i+2] = tmp
                    self.max_heapify(nums,2*i+2,n)
            else:
                if nums[i] < nums[2*i+1]:
                    tmp = nums[i]
                    nums[i] = nums[2*i+1]
                    nums[2*i+1] = tmp
                    self.max_heapify(nums,2*i+1,n)

    def min_heapify(self,nums,i,n):
        if 2*i+1 == n-1:
            if nums[i] > nums[2*i+1]:
                tmp = nums[i]
                nums[i] = nums[2*i+1]
                nums[2*i+1] = tmp
                self.min_heapify(nums,2*i+1,n)
        elif 2*i+2 < n:
            if nums[2*i+1] >= nums[2*i+2]:
                if nums[i] > nums[2*i+2]:
                    tmp = nums[i]
                    nums[i] = nums[2*i+2]
                    nums[2*i+2] = tmp
                    self.min_heapify(nums,2*i+2,n)
            else:
                if nums[i] > nums[2*i+1]:
                    tmp = nums[i]
                    nums[i] = nums[2*i+1]
                    nums[2*i+1] = tmp
                    self.min_heapify(nums,2*i+1,n)

    def min_heappush(self,num,A,k):
        if A[0] < num:
            A[0] = num
            self.min_heapify(A,0,k)

    def topk(self,nums,k):
        n = len(nums)
        k = min(n,k)
        heap = nums[:k]
        for i in range(k//2-1,-1,-1):
            self.min_heapify(heap,i,k)
            
        for i in range(k,n):
            self.min_heappush(nums[i],heap,k)
        
        res = []
        for i in range(k):
            res.append(heap[0])
            heap[0] = heap[k-1-i]
            self.min_heapify(heap,0,k-1-i)
        return res[::-1]
            
if __name__ == "__main__":
    obj = Solution()
    print(obj.topk([3,10,1000,-99,4,100], 3))
    #print(obj.topk([], 3))
