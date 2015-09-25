
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = ''.join(sorted(s))
        y = ''.join(sorted(t))
        return x == y

    def isAnagram_2(self, s, t):
        pool = {}
        for x in s:
            pool[x] = pool.get(x, 0) + 1
        for x in t:
            pool[x] = pool.get(x, 0) - 1
        return all(x == 0 for x in pool.itervalues())

def main():
    inputs = [("anagram", "nagaram"), ("rat", "car")]
    for s, t in inputs:
        result = Solution().isAnagram_2(s, t)
        print result

if __name__ == '__main__':
    main()
