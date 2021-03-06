
class DirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.has_cycle = False
        result = []
        G = self.buildGraph(numCourses, prerequisites)
        visited = [False] * numCourses
        on_stack = [False] * numCourses
        for i in xrange(numCourses):
            if not visited[i]:
                self.dfs_1(G[i], visited, on_stack, result)
        result.reverse()
        return [] if self.has_cycle else result

    def buildGraph(self, numCourses, prerequisites):
        G = [DirectedGraphNode(i) for i in xrange(numCourses)]
        for u, v in prerequisites:
            G[v].neighbors.append(G[u])
        return G

    def dfs_1(self, v, visited, on_stack, result):
        # recursion: post-order
        visited[v.label] = True
        on_stack[v.label] = True

        for neighbor in v.neighbors:
            if self.has_cycle:
                return
            if not visited[neighbor.label]:
                self.dfs_1(neighbor, visited, on_stack, result)
            elif on_stack[neighbor.label]:
                self.has_cycle = True

        on_stack[v.label] = False
        result.append(v.label)

    def dfs_0(self, v, visited, result):
        # iteration: pre-order
        stack = [v]
        while stack:
            w = stack.pop()
            if not visited[w.label]:
                result.append(w.label)
                visited[w.label] = True
                for neighbor in w.neighbors:
                    stack.append(neighbor)

def main():
    inputs = [(2, [[1,0]])]
    inputs += [(4, [[1,0],[2,0],[3,1],[3,2]])]
    inputs += [(3, [[1,0],[2,1],[0,2]])]
    for numCourses, prerequisites in inputs:
        result = Solution().findOrder(numCourses, prerequisites)
        print result

if __name__ == '__main__':
    main()
