
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        lv1 = version1.split('.')
        lv2 = version2.split('.')
        sz_lv1 = len(lv1)
        sz_lv2 = len(lv2)
        for i in xrange(max(sz_lv1, sz_lv2)):
            v1 = int(lv1[i]) if i < sz_lv1 else 0
            v2 = int(lv2[i]) if i < sz_lv2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

def main():
    inputs = [('1.1', '1'), ('1', '1.0'), ('0.1', '1.1'), ('1.1', '1.2')]
    for v1, v2 in inputs:
        result = Solution().compareVersion(v1, v2)
        print result

if __name__ == '__main__':
    main()
