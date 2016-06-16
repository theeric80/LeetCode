
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        """
        return self.construct(nodes, 0) == len(nodes)-1
        """
        return self.isValidSerialization_0(nodes)

    def construct(self, preorder, i):
        if i >= len(preorder):
            return i
        elif preorder[i] == '#':
            return i

        l = self.construct(preorder, i+1)  # l: the last node of left subtree
        r = self.construct(preorder, l+1)  # r: the last node of right subtree
        return r

    def isValidSerialization_0(self, preorder):
        # use stack
        # https://leetcode.com/discuss/83825/simple-python-solution-using-stack-with-explanation
        s = []
        for n in preorder:
            s.append(n)
            while len(s) >= 2 and s[-1] == '#' and s[-2] == '#':
                s = s[:-2]
                if len(s) == 0:
                    return False
                s.pop()
                s.append('#')
        return len(s) == 1 and s[-1] == '#'

def main():
    inputs= ['9,3,4,#,#,1,#,#,2,#,6,#,#', '9,#,#,1', '1,#']
    for preorder in inputs:
        result = Solution().isValidSerialization(preorder)
        print '{}: {}'.format(preorder, result)

if __name__ == '__main__':
    main()
