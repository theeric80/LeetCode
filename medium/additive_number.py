
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        result, stack = [], []
        return self.isAdditiveNumber_0(num, 0, stack, result)

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
