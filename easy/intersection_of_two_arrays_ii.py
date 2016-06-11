
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return self.intersect_2(nums1, nums2)

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

    def intersect_2(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        i, j, m, n = 0, 0, len(nums1), len(nums2)
        result = []
        while i < m and j < n:
            a, b = nums1[i], nums2[j]
            if a == b:
                result.append(a)
                i += 1
                j += 1
            elif a < b:
                i += 1
            elif a > b:
                j += 1
        return result

def main():
    inputs = [[[1,2,2,1],[2,2]],]
    for nums1, nums2 in inputs:
        result = Solution().intersect(nums1, nums2)
        print '{} + {} = {}'.format(nums1, nums2, result)

if __name__ == '__main__':
    main()
