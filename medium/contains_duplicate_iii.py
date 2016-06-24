
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        return self.containsNearbyAlmostDuplicate_1(nums, k, t)

    def containsNearbyAlmostDuplicate_1(self, nums, k, t):
        """
        i != j
        abs(i - j) <= k
        abs(nums[i] - nums[j]) <= t
        """
        n = len(nums)
        for j in xrange(n):
            for i in xrange(n):
                if i != j and abs(i - j) <= k and abs(nums[i] - nums[j]) <= t:
                    return True
        return False

    def containsNearbyAlmostDuplicate_1(self, nums, k, t):
        import bisect
        window = []
        for i, n in enumerate(nums):
            # find the ceiling of n-t in window
            j = bisect.bisect_left(window, n-t)
            if not window or j >= len(window):
                pass
            # window[j]: ceiling -> n - t <= ceiling
            # check -> ceiling -t <= n
            elif window[j]-t <= n:
                return True
            bisect.insort_left(window, n)
            if i >= k:
                window.remove(nums[i-k])
        return False

def main():
    nums = [2,1]
    k, t = 1, 1
    result = Solution().containsNearbyAlmostDuplicate(nums, k, t)
    print nums
    print '({}, {}) = {}'.format(k, t, result)

    nums = [4,2,1]
    result = Solution().containsNearbyAlmostDuplicate(nums, k, t)
    print nums
    print '({}, {}) = {}'.format(k, t, result)

    nums = [2,4,6]
    result = Solution().containsNearbyAlmostDuplicate(nums, k, t)
    print nums
    print '({}, {}) = {}'.format(k, t, result)

if __name__ == '__main__':
    main()
