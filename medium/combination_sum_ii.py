
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result, sum_ = [], []
        if candidates:
            self.combinationSum_0(sorted(candidates), target, 0, sum_, result)
        return result

    def combinationSum_0(self, candidates, target, i, sum_, result):
        if target < 0:
            return
        elif target == 0:
            result.append(sum_[:])
            return

        for j in xrange(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]:  # remove duplicates
                continue
            v = candidates[j]
            sum_.append(v)
            self.combinationSum_0(candidates, target-v, j+1, sum_, result)
            sum_.pop()

def main():
    inputs = [([10,1,2,7,6,1,5], 8),]
    for candidates, target in inputs:
        result = Solution().combinationSum2(candidates, target)
        print result

if __name__ == '__main__':
    main()
