#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181230
#
################################################################################

"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        if self.dfs(head):
            newhead = ListNode(1)
            newhead.next = head
            head = newhead
        return head
        
    def dfs(self,node):
        if not node.next:
            if node.val is 9:
                node.val = 0
                return True
            else:
                node.val += 1
                return False
        else:
            if self.dfs(node.next):
                if node.val is 9:
                    node.val = 0
                    return True
                else:
                    node.val += 1
                    return False

if __name__ == "__main__":
    head = ListNode(9)
    head.next = ListNode(9)
    head.next.next = ListNode(9)

    obj = Solution()
    head = obj.plusOne(head)
    while head:
        print(head.val)
        head = head.next

