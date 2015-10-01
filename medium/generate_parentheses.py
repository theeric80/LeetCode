
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        curr, result = "", []
        self.generateParenthesis_0(n, 0, 0, curr, result)
        return result

    def generateParenthesis_0(self, n, l, r, curr, result):
        # backtracing
        if l == n and r == n:
            result.append(curr)
            return

        if l < n:
            curr += '('
            self.generateParenthesis_0(n, l+1, r, curr, result)
            curr = curr[:-1]

        if r < l:
            curr += ')'
            self.generateParenthesis_0(n, l, r+1, curr, result)
            curr = curr[:-1]

def main():
    inputs = [3, 0, 1]
    for n in inputs:
        result = Solution().generateParenthesis(n)
        print result

if __name__ == '__main__':
    main()
