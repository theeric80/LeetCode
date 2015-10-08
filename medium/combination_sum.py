
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result, sum_ = [], []
        if candidates:
            self.combinationSum_0(sorted(candidates), target, sum_, result)
        return result

    def combinationSum_0(self, candidates, target, sum_, result):
        if target < 0:
            return
        elif target == 0:
            result.append(sum_[:])
            return

        i, sz = 0, len(candidates)
        for i in xrange(sz):
            v = candidates[i]
            sum_.append(v)
            self.combinationSum_0(candidates[i:], target-v, sum_, result)
            sum_.pop()

def main():
    inputs = [([2,3,6,7], 7),]
    inputs = [([8,7,4,3], 11),]
    for candidates, target in inputs:
        result = Solution().combinationSum(candidates, target)
        print result

if __name__ == '__main__':
    main()
