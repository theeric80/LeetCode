
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2: return x
        return self.mySqrt_0(x)

    def mySqrt_1(self, x):
        # binary search
        lo, hi = 1, x
        while lo+1 < hi:
            mid = lo + (hi-lo)/2
            if mid > x/mid:
                hi = mid
            else:
                # mid <= x/mid:
                lo = mid
        return lo

    def mySqrt_0(self, x):
        # binary search
        lo, hi = 1, x
        result = lo
        while lo <= hi:
            # overflow
            # 1) mid = (lo+hi) / 2 
            # 2) mid*mid > x
            mid = lo + (hi-lo)/2
            if mid > x/mid:
                hi = mid - 1
            elif mid < x/mid:
                lo = mid + 1
                result = mid
            else:
                return mid
        return result

def main():
    inputs = [1,4,6,10]
    for x in inputs:
        result = Solution().mySqrt(x)
        print x, result

if __name__ == '__main__':
    main()
