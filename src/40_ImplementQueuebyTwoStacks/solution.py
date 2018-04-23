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
class MyStack:
        
    def __init__(self):
        self.list = []
   
    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False
   
    def push(self, x):
        self.list.append(x)
   
    def pop(self):
        return self.list.pop()
   
    def top(self):
        return self.list[-1]

class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = MyStack()
        self.work = MyStack()
        
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        
        while not self.stack.isEmpty():
            nn = self.stack.pop()
            self.work.push(nn)

        self.stack.push(element)

        while not self.work.isEmpty():
            nn = self.work.pop()
            self.stack.push(nn)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here

        return self.stack.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack.list[-1]

if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    print q.stack.list
    print q.pop()
    q.push(2)
    q.push(3)
    print q.stack.list
    print q.top()
    print q.pop()
