
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        H = dict()
        n = len(s)
        for i in xrange(10, n+1):
            dna = s[i-10:i]
            key = hash(dna)
            if key not in H:
                H[key] = 1
            elif H[key] == 1:
                H[key] = 2
                result.append(dna)
        return result

def main():
    inputs = ['AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT']
    inputs += ['AAAAAAAAAAAA']
    for s in inputs:
        result = Solution().findRepeatedDnaSequences(s)
        print result

if __name__ == '__main__':
    main()
