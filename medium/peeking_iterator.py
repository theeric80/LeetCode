
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self._pos = 0
        self._iterable = nums[:]

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self._pos < len(self._iterable)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        result = self._iterable[self._pos]
        self._pos += 1
        return result

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterable = iterator
        self._element = None
        self.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._element

    def next(self):
        """
        :rtype: int
        """
        result = self._element
        if self._iterable:
            self._element = self._iterable.next() if self._iterable.hasNext() else None
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self._element is not None)

def main():
    nums = [1,2,3]
    iterator = PeekingIterator(Iterator(nums))
    while iterator.hasNext():
        print iterator.peek()
        print iterator.next()

if __name__ == '__main__':
    main()
