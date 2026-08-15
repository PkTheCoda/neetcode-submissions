class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        F = [1] * (n+1)
        print(F)

        F[0] = 1
        F[1] = 1

        for i in range(2, n+1):
            F[i] = F[i-1] + F[i-2]

        return F[n]