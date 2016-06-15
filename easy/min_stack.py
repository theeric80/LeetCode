
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._s = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        m = self.getMin()
        m = x if m is None else min(x, m)
        self._s.append((x, m))

    def pop(self):
        """
        :rtype: void
        """
        self._s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._s[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self._s[-1][1] if self._s else None

def main():
    minStack = MinStack()
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)

    print minStack.getMin()
    minStack.pop()
    print minStack.top()
    print minStack.getMin()

if __name__ == '__main__':
    main()
