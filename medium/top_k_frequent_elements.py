
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return self.top_3(nums, k) if nums else []

    def top_1(self, nums, k):
        count = {}
        for n in nums:
            count[n] = count.setdefault(n, 0) + 1
        return sorted(count, key=count.get, reverse=True)[:k]

    def top_2(self, nums, k):
        count = {}
        for n in nums:
            count[n] = count.setdefault(n, 0) + 1

        import heapq
        return heapq.nlargest(k, count, key=count.get)

    def top_3(self, nums, k):
        count = {}
        for n in nums:
            count[n] = count.setdefault(n, 0) + 1

        # bucket sort
        bucket = [[] for i in xrange(len(nums)+1)]
        for key, val in count.iteritems():
            bucket[val].append(key)

        result = []
        for item in reversed(bucket):
            if len(result) >= k: break
            if not item: continue
            result.extend(item)
        return result

def main():
    nums = [4,4,4,5,5,6,6,7]
    k = 2
    result = Solution().topKFrequent(nums, k)
    print 'top {} elm in {} = {}'.format(k, nums, result)

if __name__ == '__main__':
    main()
