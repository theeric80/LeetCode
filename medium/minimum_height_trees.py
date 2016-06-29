
class Graph(object):
    def __init__(self, n, edges):
        object.__init__(self)
        self._v = n
        self._adj = [[] for i in xrange(n)]
        for e in edges:
            self.add_edge(*e)

    def V(self):
        return self._v

    def add_edge(self, v, w):
        self._adj[v].append(w)
        self._adj[w].append(v)

    def adj(self, v):
        return self._adj[v]

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        return self.findMinHeightTrees_0(n, edges)

    def findMinHeightTrees_0(self, n, edges):
        min_h = n
        result = []
        G = Graph(n, edges)
        for v in xrange(n):
            h = self.bfs(G, v)
            if h < min_h:
                result, min_h = [v], h
            elif h == min_h:
                result.append(v)
        return result

    def bfs(self, G, v):
        n = G.V()
        marked = [False] * n
        length = [0] * n

        marked[v] = True
        q = [v]

        while q:
            v = q.pop(0)
            for w in G.adj(v):
                if not marked[w]:
                    marked[w] = True
                    length[w] = length[v] + 1
                    q.append(w)
        return max(length)

def main():
    n, edges = 0, []
    result = Solution().findMinHeightTrees(n, edges)
    print 'root of MHTs = {}'.format(result)

    n, edges = 1, []
    Solution().findMinHeightTrees(n, edges)
    result = Solution().findMinHeightTrees(n, edges)
    print 'root of MHTs = {}'.format(result)

    n, edges = 2, [[0, 1]]
    Solution().findMinHeightTrees(n, edges)
    result = Solution().findMinHeightTrees(n, edges)
    print 'root of MHTs = {}'.format(result)

    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    result = Solution().findMinHeightTrees(n, edges)
    print 'root of MHTs = {}'.format(result)

    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    result = Solution().findMinHeightTrees(n, edges)
    print 'root of MHTs = {}'.format(result)

if __name__ == '__main__':
    main()
