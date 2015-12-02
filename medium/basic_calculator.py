
class Solution(object):
    operators = set(['(', ')', '+', '-'])
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            postfix = self.infix_to_postfix(s)
            return self.calculate_postfix(postfix)
        return 0

    def calculate_postfix(self, postfix):
        operators = Solution.operators
        stack = []
        for token in postfix:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
        return stack[-1]

    def infix_to_postfix(self, s):
        operators = Solution.operators
        def next_token(s):
            operand = ''
            for c in s:
                if c == ' ':
                    continue
                elif c in operators:
                    if operand:
                        yield operand
                        operand = ''
                    yield c
                else:
                    operand += c

            if operand:
                yield operand

        result = []
        stack = []
        for token in next_token(s):
            if token not in operators:
                result.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack:
                    op = stack.pop()
                    if op == '(': break
                    result.append(op)
            else:
                while stack:
                    op = stack[-1]
                    if op == '(':
                        break
                    else:
                        # TODO: the precedence of the op
                        result.append(stack.pop())
                stack.append(token)
        result += stack[::-1]
        return result

def main():
    inputs = ['', '1', '1 + 1']
    inputs += [' 2-1 + 2 ']
    inputs += ['(1+(4+5+2)-3)+(6+8)']
    for s in inputs:
        result = Solution().calculate(s)
        print '{0} = {1}'.format(s, result)

if __name__ == '__main__':
    main()
