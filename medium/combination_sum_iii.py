
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result, sum_ = [], []
        self.combinationSum_0(k, n, 1, sum_, result)
        return result

    def combinationSum_0(self, k, n, i, sum_, result):
        if n < 0:
            return
        elif k == 0:
            if n == 0:
                result.append(sum_[:])
            return

        for j in xrange(i, 10):
            sum_.append(j)
            self.combinationSum_0(k-1, n-j, j+1, sum_, result)
            sum_.pop()

def main():
    inputs = [(3,7), (3,9),]
    for k, n in inputs:
        result = Solution().combinationSum3(k, n)
        print result

if __name__ == '__main__':
    main()
