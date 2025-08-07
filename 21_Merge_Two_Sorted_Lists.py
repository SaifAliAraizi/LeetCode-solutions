# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):  # For printing the list nicely
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a new dummy node to simplify the code
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            # Compare the values of the current nodes in both lists
            if list1.val < list2.val:
                # If the value of the current node in list1 is smaller, append it to the result
                current.next = list1
                list1 = list1.next
            else:
                # If the value of the current node in list2 is smaller, append it to the result
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # If there are remaining nodes in either list, append them to the result
        current.next = list1 if list1 else list2
        # Return the result
        return dummy.next

solution = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged = solution.mergeTwoLists(list1, list2)
print(merged)  # Output: 1 -> 1


"""
21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""