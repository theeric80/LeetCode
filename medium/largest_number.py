
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums:
            return self.largestNumber_0(nums)
        return ''

    def largestNumber_0(self, nums):
        n = len(nums)
        N = len(str(max(nums)))
        result = map(str, nums)
        self.sort(result, 0, n-1, 0, N)
        result.reverse()
        return ''.join(result)

    def sort(self, nums, lo, hi, d, N):
        if hi <= lo or d >= N:
            return

        R = 10 + 2
        count = [0] * R
        aux = nums[:]
        for i in xrange(lo, hi+1):
            count[self.char(nums[i], d)+2] += 1

        for i in xrange(0, R-1):
            count[i+1] += count[i]

        for i in xrange(lo, hi+1):
            n = self.char(aux[i], d) + 1
            j = count[n]
            nums[j] = aux[i]
            count[n] += 1

        for i in xrange(R-2):
            self.sort(nums, lo+count[i], lo+count[i+1]-1, d+1, N)

    def char(self, s, d):
        n = len(s)
        return int(s[d]) if d < n else -1

def main():
    inputs = [[3,30,34,5,9]]
    #inputs = [[3,2,1,0,3,3,2]]
    for nums in inputs:
        result = Solution().largestNumber(nums)
        print result

if __name__ == '__main__':
    main()
