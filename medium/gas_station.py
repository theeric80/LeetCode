
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        return self.canCompleteCircuit_0(gas, cost)

    def canCompleteCircuit_0(self, gas, cost):
        sz = len(gas)
        d = [gas[i]-cost[i] for i in xrange(sz)]
        remain, j = d[0], 0
        route = [0]
        for i in xrange(sz): 
            while remain >= 0:
                if len(route) == sz:
                    return i
                j = (j+1) % sz
                remain += d[j]
                route.append(j)
            remain -= d[i]
            route.pop(0)
        return -1

def main():
    gas, cost = [1,2,3,], [1,2,3,]
    gas, cost = [1,2,3,], [1,3,3,]
    gas, cost = [1,2,4,], [2,2,3,]
    result = Solution().canCompleteCircuit(gas, cost)
    print result

if __name__ == '__main__':
    main()
