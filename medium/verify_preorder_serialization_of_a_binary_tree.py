
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        return self.construct(nodes, 0) == len(nodes)-1

    def construct(self, preorder, i):
        if i >= len(preorder):
            return i
        elif preorder[i] == '#':
            return i

        l = self.construct(preorder, i+1)  # l: the last node of left subtree
        r = self.construct(preorder, l+1)  # r: the last node of right subtree
        return r

def main():
    inputs= ['9,3,4,#,#,1,#,#,2,#,6,#,#', '9,#,#,1', '1,#']
    for preorder in inputs:
        result = Solution().isValidSerialization(preorder)
        print '{}: {}'.format(preorder, result)

if __name__ == '__main__':
    main()
