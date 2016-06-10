
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = list(s)
        vowels = set('aeiouAEIOU')
        i, j, n, = -1, len(a), len(a)
        while True:
            while True:
                i += 1
                if i >= n or a[i] in vowels: break
            while True:
                j -= 1
                if j < 0 or a[j] in vowels: break
            if i < j:
                a[i], a[j] = a[j], a[i]
            else:
                break
        return ''.join(a)

def main():
    inputs = ['', 'a', 'b', 'ab', 'hello', 'leetcode', 'aA']
    for s in inputs:
        result = Solution().reverseVowels(s)
        print '{} = {}'.format(s, result)

if __name__ == '__main__':
    main()
