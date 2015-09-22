
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True

        h = dict()
        u = set()
        for i, sc in enumerate(s):
            tc, hc = t[i], h.get(sc)
            if hc is not None and hc != tc:
                return False
            elif hc is None and tc in u:
                # The 2nd sc that maps to the same tc
                return False
            h[sc] = tc
            u.add(tc)
        return True

def main():
    inputs = [('egg', 'add'), ('foo', 'bar'), ('ab', 'aa'), ('ba', 'aa')]
    for s, t in inputs:
        result = Solution().isIsomorphic(s, t)
        print s, t, result

if __name__ == '__main__':
    main()
