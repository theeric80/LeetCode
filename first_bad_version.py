# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    return False if version < 5 else True

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        return self.firstBadVersion_1(1, n)

    def firstBadVersion_1(self, l, h):
        # non-recursive
        while h > l:
            mid = (l+h) / 2
            if isBadVersion(mid):
                h = mid
            else:
                l = mid + 1
        return l

    def firstBadVersion_0(self, l, h):
        # recursive
        if h < l:
            return 0
        mid = (l+h) / 2
        if not isBadVersion(mid):
            return self.firstBadVersion_0(mid+1, h)
        elif isBadVersion(mid) and ((mid == l) or (not isBadVersion(mid-1))):
            return mid
        else:
            return self.firstBadVersion_0(l, mid-1)

def main():
    inputs = [10]
    for n in inputs:
        result = Solution().firstBadVersion(n)
        print result

if __name__ == '__main__':
    main()
