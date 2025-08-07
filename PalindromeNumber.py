class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original_number = x
        reverse = 0

        for _ in str(x):
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        if(original_number == reverse):
            return True
        else:
            return False

solution = Solution()
s = 121
solution.isPalindrome(s)