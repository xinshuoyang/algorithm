"""
Definition of ListNode
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next



#class Solution:
#    """
#    @param: head: The first node of linked list.
#    @return: True if it has a cycle, or false
#    """
#    def hasCycle(self, head):
#        # write your code here
#        visited = set() 
#        return self.helper(head, visited)
#
#    def helper(self, head, visited):
#        if head is None:
#            return False
#        else:
#            if head in visited:
#                return True
#            else:
#                visited.add(head)
#                return self.helper(head.next, visited)

# version 2: without using extra memory
class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head is None:
            return False
        else:

            p1 = head
            p2 = head

            while p1.next is not None:
                if p1.next.next is not None:
                    p1 = p1.next.next
                    p2 = p2.next

                    if p1 is p2:
                        return True
                else:
                    return False

            return False
if __name__ == '__main__':
    root = ListNode(-21)
    root.next = ListNode(10)
    root.next.next = ListNode(4)

    s = Solution()
    print s.hasCycle(root)