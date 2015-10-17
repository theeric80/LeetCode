
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        return self.convert_0(s, numRows)

    def convert_0(self, s, numRows):
        line = ['' for i in  xrange(numRows)]
        i, d = 0, 1
        for x in s:
            line[i] += x
            if i <= 0:
                d = 1
            elif i >= numRows-1:
                d = -1
            i += d
        return ''.join(line)

def main():
    inputs = [('PAYPALISHIRING', 3), ('A', 1), ('AB', 1)]
    for s, numRows in inputs:
        result = Solution().convert(s, numRows)
        print result

if __name__ == '__main__':
    main()
