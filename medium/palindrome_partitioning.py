
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        #return self.partition_0(s, 0)
        part, result = [], []
        self.partition_1(s, 0, part, result)
        return result

    def partition_1(self, s, first, part, result):
        sz =  len(s)
        if first >= sz:
            result.append(part[:])
            return

        for i in xrange(first, sz):
            a = s[first:i+1]
            if self.palindrome(a):
                part.append(a)
                self.partition_1(s, i+1, part, result)
                part.pop()

    def partition_0(self, s, first):
        sz, end = len(s), len(s)-1
        if first > end:
            return [[]]
        elif first == end:
            return [[s[-1]]]

        result = []
        for i in xrange(first, sz):
            a = s[first:i+1]
            if self.palindrome(a):
                for b in self.partition_0(s, i+1):
                    result.append([a]+ b)
        return result

    def palindrome(self, s):
        return s == s[::-1]

def main():
    inputs = ['aab', 'a', 'aa', 'abbb', 'abbc']
    for s in inputs:
        result = Solution().partition(s)
        print result

if __name__ == '__main__':
    main()
