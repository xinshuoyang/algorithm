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

class SetOfStacks2:
    """
    @param: capacity: an inetger, capacity of sub stack
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.stack = [[]]

    """
    @param: v: An integer
    @return: nothing
    """
    def push(self, v):
        # write your code here
        if len(self.stack[-1]) < self.capacity:
            self.stack[-1].append(v)
        else:
            self.stack.append([v])
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.stack[-1]) is 0:
            self.stack.pop()
        return self.stack[-1].pop()

    """
    @param: index: The index of a specific sub-stack
    @return: top element of the specific sub-stack
    """
    def popAt(self, index):
        # write your code here
        if len(self.stack[-1]) is 0:
            self.stack.pop()
        v = self.stack[index].pop()
        for i in range(index+1,len(self.stack)):
            self.stack[i-1].append(self.stack[i].pop(0))
        return v

if __name__ == "__main__":
    obj = SetOfStacks2(2)
    obj.push(1)
    obj.push(2)
    obj.push(4)
    obj.push(8)
    obj.push(16)
    print(obj.popAt(0))
    print(obj.popAt(0))
    print(obj.pop())
