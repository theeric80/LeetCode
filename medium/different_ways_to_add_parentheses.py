
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.diffWaysToCompute_0(self.split(input))

    def split(self, input):
        ops = set(['+', '-', '*'])
        def nextop():
            for i, s in enumerate(input):
                if s in ops:
                    yield i

        result, i = [], 0
        for j in nextop():
            result.append(int(input[i:j]))
            result.append(input[j])
            i = j + 1
        if input:
            result.append(int(input[i:]))
        return result

    def diffWaysToCompute_0(self, input):
        sz = len(input)
        if sz == 1:
            return input

        result = []
        for j in xrange(1, sz, 2):
            for a in self.diffWaysToCompute_0(input[:j]):
                for b in self.diffWaysToCompute_0(input[j+1:]):
                    if input[j] == '+':
                        result.append(a + b)
                    elif input[j] == '-':
                        result.append(a - b)
                    elif input[j] == '*':
                        result.append(a * b)
        return result

def main():
    inputs = ["2-1-1", "2*3-4*5", "10+5", "0"]
    for s in inputs:
        result = Solution().diffWaysToCompute(s)
        print result

if __name__ == '__main__':
    main()
