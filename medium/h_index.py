
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        return self.hIndex_0(citations)

    def hIndex_1(self, citations):
        sz = len(citations)
        count = [0] * (sz+1)
        for n in citations:
            if n > sz:
                count[sz] += 1
            else:
                count[n] += 1

        total = 0
        for i in xrange(sz, -1, -1):
            total += count[i]
            if total >= i:
                return i
        return 0

    def hIndex_0(self, citations):
        citations.sort(reverse=True)
        for i, n in enumerate(citations, 1):
            if i > n:
                return i-1
        return i

    def qsort(self, citations, lo, hi):
        if lo < hi:
            j = self.partition(citations, lo, hi)
            self.qsort(citations, lo, j)
            self.qsort(citations, j+1, hi)

    def partition(self, citations, lo, hi):
        v = citations[lo]
        i, j = lo-1, hi+1
        while True:
            while True:
                j -= 1
                if citations[j] <= v: break
            while True:
                i += 1
                if citations[i] >= v: break
            if i < j:
                citations[i], citations[j] = citations[j], citations[i]
            else:
                return j

def main():
    inputs = [[3,0,6,1,5], [2,0,1,2], [0], [6]]
    for citations in inputs:
        result = Solution().hIndex(citations)
        print citations, result

if __name__ == '__main__':
    main()
