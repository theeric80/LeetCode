
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        w1, h1 = C-A, D-B
        w2, h2 = G-E, H-F

        a1 = w1*h1 + w2*h2
        if G <= A or E >= C or F >= D or H <= B:
            return a1

        I, J, K, L = max(A,E), max(B,F), min(C,G), min(D,H)
        w3, h3 = K-I, L-J
        return a1 - w3*h3

def main():
    inputs = [-3,0, 3,4, 0,-1, 9,2]
    result = Solution().computeArea(*inputs)
    print result

if __name__ == '__main__':
    main()
