
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return self.intersect_1(nums1, nums2)

    def intersect_1(self, nums1, nums2):
        count = {}
        for n in nums1:
            count[n] = count.setdefault(n, 0) + 1

        result = []
        for n in nums2:
            if count.has_key(n) and count[n] > 0:
                result.append(n)
                count[n] -= 1
        return result

def main():
    inputs = [[[1,2,2,1],[2,2]],]
    for nums1, nums2 in inputs:
        result = Solution().intersect(nums1, nums2)
        print '{} + {} = {}'.format(nums1, nums2, result)

if __name__ == '__main__':
    main()
