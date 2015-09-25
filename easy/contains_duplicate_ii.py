
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        return self.containsNearbyDuplicate_0(nums, k)

    def containsNearbyDuplicate_1(self, nums, k):
        if not nums:
            return False

        s = set()
        for i, n in enumerate(nums):
            if (i > k):
                # move sllding window
                s.remove(nums[i-k-1])
            if n in s:
                return True
            s.add(n)

        return False

    def containsNearbyDuplicate_0(self, nums, k):
        if not nums:
            return False

        h = {}
        for i, n in enumerate(nums):
            j = h.get(n)
            if j is not None and (i-j) <= k:
                return True
            h[n] = i

        return False

def main():
    inputs = [(1, 0, 1, 1), (1, 0, 1, 2)]
    for nums in inputs:
        k = 1
        result = Solution().containsNearbyDuplicate(nums, k)
        print nums, k, result

if __name__ == '__main__':
    main()
