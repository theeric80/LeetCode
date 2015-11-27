
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

def main():
    board = [['A','B','C','E'],
             ['S','F','C','S'],
             ['A','D','E','E']]
    inputs = ['ABCCED', 'SEE', 'ABCB']
    for word in inputs:
        result = Solution().exist(board, word)
        print '{0}: {1}'.format(word, result)

if __name__ == '__main__':
    main()
