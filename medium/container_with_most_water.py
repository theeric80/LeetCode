
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo, hi = 0, len(height)-1
        result = 0
        while lo < hi:
            area = min(height[lo], height[hi]) * (hi-lo)
            result = max(result, area)
            if height[lo] < height[hi]:
                while True:
                    lo += 1
                    if lo >= hi or height[lo] > height[lo-1]: break
            else:
                while True:
                    hi -= 1
                    if lo >= hi or height[hi] > height[hi+1]: break
        return result

def main():
    inputs = [(1,1,3,2,3), (1,)]
    for height in inputs:
        result = Solution().maxArea(height)
        print result

if __name__ == '__main__':
    main()
