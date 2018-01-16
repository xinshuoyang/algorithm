#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180116
#
################################################################################

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
"""
class RandomListNode:
   def __init__(self, x):
       self.label = x
       self.next = None
       self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here

        if head == None:
            return None

        maps = {}
        
        # make a copy of all nodes

        p = head

        while p != None:
            maps[p] = RandomListNode(p.label)
            p = p.next

        # add relationships

        p = head

        while p != None:
            if p.next != None:
                maps[p].next = maps[p.next]
            if p.random != None:
                maps[p].random = maps[p.random]
            
            p = p.next

        return maps[head]


if __name__ == '__main__':

    s = Solution()
    
    n1 = None

#    n1 = RandomListNode(1)
#    n2 = RandomListNode(2)
#    n3 = RandomListNode(3)
#    
#    n1.next = n2
#    n2.next = n3
#    
#    n1.random = n3
#    n2.random = n1
#    n3.random = n2

    cn1 = s.copyRandomList(n1)

#    print cn1.label, cn1.next.label, cn1.next.next.label
#    print cn1.random.label, cn1.next.random.label, cn1.next.next.random.label
