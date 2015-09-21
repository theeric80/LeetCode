
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' and (not stack or stack.pop() != '('):
                return False
            elif c == ']' and (not stack or stack.pop() != '['):
                return False
            elif c == '}' and (not stack or stack.pop() != '{'):
                return False
        return len(stack) == 0

def main():
    inputs = ['()[]{}', '(]', '([)]', ']', '[']
    for s in inputs:
        result = Solution().isValid(s)
        print result

if __name__ == '__main__':
    main()
