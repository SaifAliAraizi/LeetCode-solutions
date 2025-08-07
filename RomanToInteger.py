class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_Map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        sum = 0
        i = 0

        while( i < len(s)):

            if i + 1 < len(s) and roman_Map[s[i]] < roman_Map[s[i + 1]]:
                sum += roman_Map[s[i + 1]] - roman_Map[s[i]]
                i += 2
            else:
                sum += roman_Map[s[i]]
                i += 1

        return sum
    
solution = Solution()
s = "MCMXCIV"
print(solution.romanToInt(s)) # Output: 9
                

