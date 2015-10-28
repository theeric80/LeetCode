
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.cycle = False

        G = self.buildGraph(numCourses, prerequisites)

        result, marked, on_stack = [], [False]*len(G), [False]*len(G)
        for v in G:
            if not marked[v.label]:
                self.topological_sort(G, v, marked, on_stack, result)
        result.reverse()

        return not self.cycle

    def buildGraph(self, numCourses, prerequisites):
        G = [UndirectedGraphNode(i) for i in xrange(numCourses)]
        for u, v in prerequisites:
            G[u].neighbors.append(G[v])
        return G

    def topological_sort(self, G, v, marked, on_stack, result):
        label = v.label
        marked[label] = True
        on_stack[label] = True
        for w in v.neighbors:
            if self.cycle:
                return
            if not marked[w.label]:
                self.topological_sort(G, w, marked, on_stack, result)
            elif on_stack[w.label]:
                self.cycle = True

        on_stack[label] = False
        result.append(label)

    def dfs(self, G, v):
        result, marked = [], [False]*len(G)
        s = [v]
        while s:
            node = s.pop()
            label = node.label
            if not marked[label]:
                marked[label] = True
                result.append(label)
                for neighbor in node.neighbors:
                    s.append(neighbor)
        print '->'.join(str(i) for i in result)


def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    inputs = [(2, [[1,0]])]
    for numCourses, prerequisites in inputs:
        result = Solution().canFinish(numCourses, prerequisites)
        print result

if __name__ == '__main__':
    main()
