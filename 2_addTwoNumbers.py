# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = Solution()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            current.next = Solution(carry % 10)
            carry //= 10
            current = current.next

        return dummy.next 
            
# Helper function to convert a list to a linked list
def list_to_linked_list(nums):
    dummy = Solution()
    current = dummy
    for num in nums:
        current.next = Solution(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result           

solution = Solution()
l1 = list_to_linked_list([2, 4, 3])
l2 = list_to_linked_list([5, 6, 4])
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))