#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171204
#
################################################################################

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        
        root = node

        if node == None:
            return None

        nodes = self.getnodes(node)

        # mapping old node to new node
        mapping = {}
        for ii in nodes:
            mapping[ii] = UndirectedGraphNode(ii.label)

        # copy neighbors
        for ii in nodes:
            for jj in ii.neighbors:
                mapping[ii].neighbors.append(mapping[jj])

        return mapping[root]

    def getnodes(self, root):
        """
        get all nodes in the graph
        """
         
        res = []
        visit = {}
        
        q = [root]
        
        res.append(root)
        visit[root] = True
        
        while len(q) != 0:
            node = q.pop()

            for ii in node.neighbors:
                if not visit.has_key(ii) or not visit[ii]:
                    res.append(ii)
                    visit[ii] = True
                    q.append(ii)

        return res
