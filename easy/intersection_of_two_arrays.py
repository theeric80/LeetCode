
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return self.intersect_1(nums1, nums2)

    def intersect_1(self, nums1, nums2):
        s, result = set(nums1), set()
        [result.add(n) for n in nums2 if n in s]
        return list(result)

def main():
    inputs = [[[1,2,2,1],[2,2]],]
    for nums1, nums2 in inputs:
        result = Solution().intersect(nums1, nums2)
        print '{} + {} = {}'.format(nums1, nums2, result)

if __name__ == '__main__':
    main()
