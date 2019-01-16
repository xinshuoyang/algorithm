#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190114
#
################################################################################

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

#    """
#    heap sort
#    """
#    def sortIntegers2(self, A):
#        # write your code here
#        n = len(A)
#        for i in range(n//2-1,-1,-1):
#            self.max_heapify(A,i,n)
#        
#        for i in range(n):
#            tmp = A[0]
#            A[0] = A[n-1-i] 
#            A[n-1-i] = tmp
#            self.max_heapify(A,0,n-1-i)
#    
#    def max_heapify(self,A,i,n):
#        if 2*i+1 == n-1:
#            if A[i] < A[2*i+1]:
#                tmp = A[i]
#                A[i] = A[2*i+1]
#                A[2*i+1] = tmp
#        elif 2*i+2 < n:
#            if A[2*i+1] >= A[2*i+2]:
#                if A[i] < A[2*i+1]:
#                    tmp = A[i]
#                    A[i] = A[2*i+1]
#                    A[2*i+1] = tmp
#                    self.max_heapify(A,2*i+1,n)
#            else:
#                if A[i] < A[2*i+2]:
#                    tmp = A[i]
#                    A[i] = A[2*i+2]
#                    A[2*i+2] = tmp
#                    self.max_heapify(A,2*i+2,n)

#    """
#    quick sort
#    """
#    def sortIntegers2(self,A):
#        self.quicksort(A,0,len(A)-1)
#
#    def quicksort(self,A,low,high):
#        if low < high:
#            pivot = self.partition(A,low,high)
#            self.quicksort(A,low,pivot-1)
#            self.quicksort(A,pivot+1,high)
#
#    def partition(self,A,low,high):
#        pivot = A[high]
#        i = low-1
#        for j in range(low,high):
#            if A[j] <= pivot:
#                i += 1
#                tmp = A[i]
#                A[i] = A[j]
#                A[j] = tmp
#        tmp = A[high]
#        A[high] = A[i+1]
#        A[i+1] = tmp
#        return i+1

    """
    merge sort
    """
    def sortIntegers2(self,A):
        self.mergesort(A,0,len(A)-1)
        
    def mergesort(self,A,low,high):
        if low < high:
            mid = low+(high-low)//2

            self.mergesort(A,low,mid)
            self.mergesort(A,mid+1,high)

            self.merge(A,low,mid,high)

    def merge(self,A,low,mid,high):
        # copy the sorted arraies
        ll = []
        for i in range(low,mid+1):
            ll.append(A[i])
        rr = []
        for i in range(mid+1,high+1):
            rr.append(A[i])
        
        i = 0
        j = 0
        k = 0

        while i <= mid-low and j <= high-mid-1:
            if ll[i] <= rr[j]:
                A[low+k] = ll[i]
                i += 1
            else:
                A[low+k] = rr[j]
                j += 1
            k += 1

        while i <= mid-low:
            A[low+k] = ll[i]
            i += 1
            k += 1

        while j <= high-mid-1:
            A[low+k] = rr[j]
            j += 1
            k += 1

if __name__ == "__main__":
    obj = Solution()
    A = [3,2,1,4,5]
    obj.sortIntegers2(A)
    print(A)
