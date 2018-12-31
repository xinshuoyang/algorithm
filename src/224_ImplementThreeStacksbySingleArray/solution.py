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

class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.stack = [None]*3*size
        self.stacklen = [0,0,0]

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        # Push value into stackNum stack
        self.stack[stackNum*self.size+self.stacklen[stackNum]] = value
        self.stacklen[stackNum] += 1
        
    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        # Pop and return the top element from stackNum stack
        v = self.stack[stackNum*self.size+self.stacklen[stackNum]-1]
        self.stack[stackNum*self.size+self.stacklen[stackNum]-1] = None
        self.stacklen[stackNum] -= 1
        return v

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        # Return the top element
        return self.stack[stackNum*self.size+self.stacklen[stackNum]-1]

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        # write your code here
        return not bool(self.stacklen[stackNum])

if __name__ == "__main__":
    obj = ThreeStacks(5)
    obj.push(0, 10)
    obj.push(0, 11)
    obj.push(1, 20)
    obj.push(1, 21)
    print(obj.pop(0))
    print(obj.pop(1))
    print(obj.peek(1))
    obj.push(2,30)
    print(obj.pop(2))
    print(obj.isEmpty(2))
    print(obj.isEmpty(0))
