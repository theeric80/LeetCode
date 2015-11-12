
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if tokens:
            return self.evalRPN_0(tokens)

    def evalRPN_0(self, tokens):
        stack = []
        for token in tokens:
            if not (token=='+' or token=='-' or token=='*' or token=='/'):
                stack.append(int(token))
                continue

            r = stack.pop()
            l = stack.pop()

            if token == '+':
                stack.append(l+r)
            elif token == '-':
                stack.append(l-r)
            elif token == '*':
                stack.append(l*r)
            elif token == '/':
                stack.append(int(float(l)/r))

        return stack[0]

def main():
    inputs = [['2','1','+','3','*'],]
    inputs += [['4','13','5','/','+'],]
    inputs += [['10','6','9','3','+','-11','*','/','*','17','+','5','+'],]
    for tokens in inputs:
        result = Solution().evalRPN(tokens)
        print '{0} = {1}'.format(tokens, result)

if __name__ == '__main__':
    main()
