
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]

        j = len(digits) - 1
        for i in xrange(j, -2, -1):
            if i < 0:
                break
            elif digits[i] < 9:
                digits[i] += 1
                break
            digits[i] = 0
        return digits if i >= 0 else [1] + digits

def main():
    inputs = [[], [0], [1], [9], [1, 0, 9]]
    for n in inputs:
        result = Solution().plusOne(n)
        print result

if __name__ == '__main__':
    main()
