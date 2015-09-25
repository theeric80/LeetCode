
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._inbox = []
        self._outbox = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._inbox.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self._outbox:
            while self._inbox:
                self._outbox.append( self._inbox.pop() )

        return self._outbox.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self._outbox:
            return self._outbox[-1]
        elif self._inbox:
            return self._inbox[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._inbox) <= 0 and len(self._outbox) <= 0

def main():
    q = Queue()

    inputs = range(1, 10)
    for n in inputs:
        result = q.push(n)

    while not q.empty():
        print q.peek()
        print q.pop()

if __name__ == '__main__':
    main()
