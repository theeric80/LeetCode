
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._s1 = []
        self._s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._s1.append(x)
        if not self._s2 or x <= self.getMin():
            self._s2.append(x)

    def pop(self):
        """
        :rtype: void
        """
        x = self._s1.pop()
        if x == self.getMin():
            self._s2.pop()
        return x

    def top(self):
        """
        :rtype: int
        """
        return self._s1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._s2[-1]

def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)

    print minStack.getMin()
    print minStack.pop()
    print minStack.top()
    print minStack.getMin()

if __name__ == '__main__':
    main()
