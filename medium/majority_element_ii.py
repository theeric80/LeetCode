
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.majorityElement_1(nums)

    def majorityElement_1(self, nums):
        candidate1, candidate2, counter1, counter2 = 0, 0, 0, 0
        for n in nums:
            if n == candidate1:
                counter1 += 1
            elif n == candidate2:
                counter2 += 1
            elif counter1 == 0:
                candidate1, counter1 = n, 1
            elif counter2 == 0:
                candidate2, counter2 = n, 1
            else:
                counter1 -= 1
                counter2 -= 1
        #print candidate1, candidate2
        return [n for n in set((candidate1, candidate2)) \
            if nums.count(n) > len(nums)//3]

    def majorityElement_0(self, nums):
        # A Linear Time Majority Vote Algorithm
        candidate, counter = 0, 0
        for n in nums:
            if counter == 0:
                candidate, counter = n, 1
            else:
                counter += 1 if candidate == n else -1
        return candidate

def main():
    inputs = [(1,1,2,3),]
    inputs = [(1,1,2,2,3),]
    for nums in inputs:
        result = Solution().majorityElement(nums)
        print result

if __name__ == '__main__':
    main()
