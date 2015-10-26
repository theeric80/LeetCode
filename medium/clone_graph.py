
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        V, G = {}, {}
        if node:
            return self.cloneGraph_0(node, V, G)

    def cloneGraph_0(self, node, V, G):
        # dfs, recursive
        V[node] = True
        result = self.cloneNode(node, G)
        for x in node.neighbors:
            if not V.get(x):
                self.cloneGraph_0(x, V, G)
        return result

    def cloneNode(self, node, G):
        label = node.label
        result = G.setdefault(label, UndirectedGraphNode(label))
        for x in node.neighbors:
            n = G.setdefault(x.label, UndirectedGraphNode(x.label))
            result.neighbors.append(n)
        return result

def dfs(node):
    result = []
    s, V = [node], {}
    while s:
        n = s.pop()
        if not V.get(n):
            V[n] = True
            result.append(n.label)
            for x in n.neighbors:
                s.append(x)
    print '->'.join(str(n) for n in result)

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_oj_undirected_graph
    node = build_oj_undirected_graph([0,1,2,'#',1,2,'#',2,2])
    result = Solution().cloneGraph(node)
    dfs(result)

if __name__ == '__main__':
    main()
