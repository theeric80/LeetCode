
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return self.countBits_2(num)

    def countBits_1(self, num):
        result = [0]
        x = 1
        for i in xrange(1, num+1):
            if i > x: x *= 2
            result.append(result[i-x] + 1)
        return result

    def countBits_2(self, num):
        result = [0]
        for i in xrange(1, num+1):
            # i & i-1: remove the rightmost 1 bit
            result.append(result[i & i-1] + 1)
        return result

def main():
    inputs = [0, 1, 5, 10]
    for num in inputs:
        result = Solution().countBits(num)
        print '{}: {}'.format(num, result)

if __name__ == '__main__':
    main()
