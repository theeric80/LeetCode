
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '*': '',
            '#': '',
            }
        result, comb = [], ''
        if digits:
            letters = list(m[d] for d in digits if m[d])
            self.letterCombinations_0(letters, comb, result)
        return result

    def letterCombinations_0(self, letters, comb, result):
        if not letters:
            result.append(comb)
            return

        for x in letters[0]:
            comb += x
            self.letterCombinations_0(letters[1:], comb, result)
            comb = comb[:-1]

def main():
    inputs = ['23', '12']
    for digits in inputs:
        result = Solution().letterCombinations(digits)
        print result

if __name__ == '__main__':
    main()
