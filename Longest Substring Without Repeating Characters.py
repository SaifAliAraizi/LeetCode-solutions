class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        for i in range(n - 1):
            if s[i] == s[i+1]:
                print(len(s))
            
solution = Solution()
s = "abcabcbb"
solution.lengthOfLongestSubstring(s)