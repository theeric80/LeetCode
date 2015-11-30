
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ''

        stack = []
        for x in path.split('/'):
            if not x or x == '.':
                continue
            elif x == '..':
                if not stack: continue
                stack.pop()
            else:
                stack.append(x)
        return '/' + '/'.join(stack)

def main():
    inputs = ['/a/./b/../../c/', '/../', '/home//foo/', '', '/', '/a']
    for path in inputs:
        result = Solution().simplifyPath(path)
        print '{0} == {1}'.format(path, result)

if __name__ == '__main__':
    main()
