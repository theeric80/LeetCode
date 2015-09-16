
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._q = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        qsize = len(self._q)
        self._q.append(x)
        for i in xrange(qsize):
            self._q.append( self._q.pop(0) )

    def pop(self):
        """
        :rtype: nothing
        """
        return self._q.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self._q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._q) <= 0

def main():
    t = Stack()

    t.push(1)
    t.push(2)
    t.push(3)
    print t.top()
    print t.pop()
    print t.top()

if __name__ == '__main__':
    main()
