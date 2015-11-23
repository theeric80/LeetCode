
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        result, stack = [], []
        return self.isAdditiveNumber_0(num, 0, stack, result)

    def isAdditiveNumber_1(self, num):
        # Ref: http://leetcode.com/discuss/70119
        n = len(num)
        for i in range(1, n):
            if i > 1 and num[0] == '0':
                break
            for j in range(i+1, n):
                first, second, third = 0, i, j
                if num[second] == '0' and third > second+1:
                    break
                while third < n:
                    result = str(int(num[first:second]) + int(num[second:third]))
                    if num[third:].startswith(result):
                        first, second, third = second, third, third + len(result)
                    else:
                        break
                if third == n:
                    return True
        return False

    def isAdditiveNumber_0(self, num, i, stack, result):
        n = len(num)
        if i >= n:
            result.append(stack[:])
            return len(stack) > 2

        for j in xrange(i+1, n+1):
            x = num[i:j]
            if len(x) > 1 and x[0] == '0':
                return False

            x = int(x)
            if len(stack) < 2:
                stack.append(x)
                ret = self.isAdditiveNumber_0(num, j, stack, result)
                if ret:
                    return True
                stack.pop()
            else:
                a, b = stack[-2], stack[-1]
                if a+b == x:
                    stack.append(x)
                    ret = self.isAdditiveNumber_0(num, j, stack, result)
                    if ret:
                        return True
                    stack.pop()
                elif a+b > x:
                    continue
                else:
                    return False

        return False

def main():
    inputs = ['112358', '199100199', '1023']
    for nums in inputs:
        result = Solution().isAdditiveNumber(nums)
        print result

if __name__ == '__main__':
    main()
