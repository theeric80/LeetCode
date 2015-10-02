
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums:
            self.permute_0([], nums[:], result)
        return result

    def permute_0(self, nums1, nums2, result):
        if not nums2:
            result.append(nums1[:])
            return

        for i, n in enumerate(nums2):
            a, b = nums1+[n], nums2[:i]+nums2[i+1:]
            self.permute_0(a, b, result)

def main():
    inputs = [[1,2,3], [], [1]]
    for nums in inputs:
        result = Solution().permute(nums)
        print result

if __name__ == '__main__':
    main()
