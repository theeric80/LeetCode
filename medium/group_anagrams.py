
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        return self.groupAnagrams_0(strs)

    def groupAnagrams_0(self, strs):
        if not strs: return []
        d = dict()
        for s in strs:
            x = ''.join(sorted(s))
            d.setdefault(x, []).append(s)
        return [sorted(l) for l in d.itervalues()]

def main():
    inputs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    result = Solution().groupAnagrams(inputs)
    print result

if __name__ == '__main__':
    main()
