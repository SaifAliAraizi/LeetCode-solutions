# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # skip the duplicate
            else:
                current = current.next
        return head

# Helper function to convert a list to a linked list
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list back to a Python list
def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Testing
val = [1, 1, 2]
linked_list = list_to_linkedlist(val)

solution = Solution()
new_head = solution.deleteDuplicates(linked_list)

print("Input: head =", val)
print("Output:", linkedlist_to_list(new_head))
