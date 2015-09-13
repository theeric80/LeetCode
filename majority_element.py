
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Vote Algorithm
        candidate = nums[0]
        counter = 0
        for n in nums:
            if counter == 0:
                candidate = n
                counter = 1
            else:
                if n == candidate:
                    counter += 1
                else:
                    counter -= 1
        return candidate

def main():
    inputs = [(1, 1, 1, 2, 3), (1, 2, 1, 3, 1)]
    for n in inputs:
        result = Solution().majorityElement(n)
        print result

if __name__ == '__main__':
    main()
