
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        sep = str.split(' ')
        if len(pattern) != len(sep):
            return False

        h  = {}
        for i, p in enumerate(pattern):
            s = sep[i]
            token = h.setdefault(p, s)
            if token and token != s:
                return False
            token = h.setdefault(s, p)
            if token and token != p:
                return False
        return True


def main():
    pattern = 'abba'
    inputs = ['dog cat cat dog', 'dog cat cat fish', 'dog dog dog dog']
    for str in inputs:
        result = Solution().wordPattern(pattern, str)
        print pattern, str, result

if __name__ == '__main__':
    main()
