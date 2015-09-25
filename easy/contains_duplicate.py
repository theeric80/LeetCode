
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not (len(nums) == len(set(nums)))

def main():
    inputs = [(1, 2, 3), (1, 1, 2, 3)]
    for n in inputs:
        result = Solution().containsDuplicate(n)
        print result

if __name__ == '__main__':
    main()
