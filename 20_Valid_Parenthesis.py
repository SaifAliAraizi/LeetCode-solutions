"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping:
                # Check if stack is not empty and top of stack matches the opening bracket
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack  # True if stack is empty, False otherwise

# Test
solution = Solution()
print(solution.isValid("()"))        # True
print(solution.isValid("()[]{}"))    # True
print(solution.isValid("(]"))        # False
print(solution.isValid("([])"))      # True
print(solution.isValid("([)]"))      # False
