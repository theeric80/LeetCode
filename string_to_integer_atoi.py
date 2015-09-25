
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        string, sign = str.strip().rstrip(), 1
        if string[0] == '+':
            string, sign = string[1:], 1
        elif string[0] == '-':
            string, sign = string[1:], -1

        result = 0
        for c in string:
            d = self.c_to_d(c)
            if d < 0:
                break
            result = result * 10 + d

        # overflow
        result = min(result, 0x7fffffff) if sign>0 else min(result, 0x80000000)
        return sign * result

    def c_to_d(self, s):
        # ord('0'): 0x30
        # ord('09): 0x39
        n = ord(s) - 0x30
        if n < 0 or n > 9:
            return -1
        return n

def main():
    inputs = ['0123456789', '+1', '-1', '-', '  -0012a42', '2147483648', '-2147483648']
    for s in inputs:
        result = Solution().myAtoi(s)
        print result

if __name__ == '__main__':
    main()
