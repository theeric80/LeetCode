
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        sz = len(s)
        i = 0
        j = sz - 1
        while i < sz or j >= 0:
            while i < sz-1 and not self.is_alphanumeric(s[i]):
                i += 1
            while j >= 0 and not self.is_alphanumeric(s[j]):
                j -= 1
            if i >= j:
                break
            a, b = s[i], s[j]
            print '{}: {}, {}: {}'.format(i, a, b, j)
            if a.lower() != b.lower():
                return False
            i += 1
            j -= 1
        return True

    def is_alphanumeric(self, c):
        # 0x30: 0, 0x39: 9
        # 0x41: A, 0x5A: Z
        # 0x61: a, 0x7A, z
        ordinal = ord(c)
        if ((ordinal >= 0x30 and ordinal <= 0x39) or
            (ordinal >= 0x41 and ordinal <= 0x5A) or
            (ordinal >= 0x61 and ordinal <= 0x7A)):
            return True
        return False

def main():
    inputs = ['A man, a plan, a canal: Panama', 'race a car']
    inputs = ['a']
    inputs = [' ']
    inputs = ['.a']
    inputs = ['"`l;`` 1o1 ??;l`"']
    #inputs = ['A man, a plan, a canal: Panama', 'race a car', 'a', ' ', '.a']
    for s in inputs:
        result = Solution().isPalindrome(s)
        print result

if __name__ == '__main__':
    main()
