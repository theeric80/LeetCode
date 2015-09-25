
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        prev = 0
        result = 0
        for x in s:
            curr = m[x]
            result += curr if curr<=prev else curr - 2*prev
            prev = curr

        return result

    def romanToIntV1(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        i, size = 0, len(s)
        result = 0
        while i < size:
            token = s[i:i+2]
            if m.has_key(token):
                result += m[token]
                i += 2
            else:
                result += m[token[0]]
                i += 1

        return result

def main():
    roman = 'DCXXI'
    roman = 'MCMXCVI'
    result = Solution().romanToInt(roman)
    #result = Solution().romanToIntV1(roman)
    print result

if __name__ == '__main__':
    main()
