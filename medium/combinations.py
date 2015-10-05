
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        comb = []
        #self.combine_0(range(1, n+1), k, [], result)
        self.combine_1(n, k, 1, comb, result)
        return result

    def combine_1(self, n, k, i, comb, result):
        if k == 0:
            result.append(comb[:])
            return

        for j in xrange(i, n+1):
            comb.append(j)
            self.combine_1(n, k-1, j+1, comb, result)
            comb.pop()

    def combine_0(self, nums, k, comb, result):
        if k == 0:
            result.append(comb[:])
            return

        for i, n in enumerate(nums):
            comb.append(n)
            self.combine_0(nums[i+1:], k-1, comb, result)
            comb.pop()

def main():
    inputs = [(4,2), (4,0), (4,4)]
    for n, k in inputs:
        result = Solution().combine(n, k)
        print result

if __name__ == '__main__':
    main()
