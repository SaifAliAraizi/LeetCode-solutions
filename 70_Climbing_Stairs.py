class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1

        a = 1  # ways to reach step 0
        b = 1  # ways to reach step 1

        for _ in range(2, n + 1):
            temp = b         # store current b (ways to reach previous step)
            b = a + b        # update b to total ways to reach current step
            a = temp         # update a to previous b (shift one step forward)
            
        """
        OR -- other synatx
        a, b = 1, 1  # a = ways to climb to (n-2), b = ways to climb to (n-1)
        for _ in range(2, n + 1):
            a, b = b, a + b  # b becomes ways to climb to n
        """

        return b

solution = Solution()
n = 3
print(solution.climbStairs(n))

"""
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""
