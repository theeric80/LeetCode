
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return self.minimumTotal_1(triangle)

    def minimumTotal_1(self, triangle):
        # bottom-up
        # space: O(m)
        m = len(triangle)
        path = triangle[-1][:]
        for i in xrange(m-2, -1, -1):
            for j in xrange(0, len(triangle[i])):
                path[j] = min(path[j], path[j+1]) + triangle[i][j]
        return path[0]

    def minimumTotal_0(self, triangle):
        # top-down
        # space: O(m^2)
        m = len(triangle)
        for i in xrange(1, m):
            for j in xrange(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == i:
                    triangle[i][j] += triangle[i-1][-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])

def main():
    inputs = [[[2], [3,4], [6,5,7], [4,1,8,3]], [[2]]]
    for triangle in inputs:
        result = Solution().minimumTotal(triangle)
        print result

if __name__ == '__main__':
    main()
