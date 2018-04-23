#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180423
#
################################################################################

class Stack:
    """
    @param: x: An integer
    @return: nothing
    """

    def __init__(self):
        self.list = []
        
    def push(self, x):
        # write your code here
        self.list.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.list.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.list[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        if len(self.list) == 0:
            return True

        return False
