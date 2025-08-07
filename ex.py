# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def addTwoNumbers(l1, l2):
#     dummy = ListNode()
#     current = dummy
#     carry = 0
    
#     while l1 or l2 or carry:
#         if l1:
#             carry += l1.val
#             l1 = l1.next
#         if l2:
#             carry += l2.val
#             l2 = l2.next
#         current.next = ListNode(carry % 10)
#         carry //= 10
#         current = current.next
    
#     return dummy.next

# # Helper function to convert a list to a linked list
# def list_to_linked_list(nums):
#     dummy = ListNode()
#     current = dummy
#     for num in nums:
#         current.next = ListNode(num)
#         current = current.next
#     return dummy.next

# # Helper function to convert a linked list to a list
# def linked_list_to_list(head):
#     result = []
#     current = head
#     while current:
#         result.append(current.val)
#         current = current.next
#     return result

# # Input example
# l1 = list_to_linked_list([2, 4, 3])
# l2 = list_to_linked_list([5, 6, 4])
# result = addTwoNumbers(l1, l2)
# print(linked_list_to_list(result))  # Output: [7, 0, 8]


def compare_characters(s):
    n = len(s)
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            print(f"Character at position {i} is equal to character at position {i + 1}.")
            print(len(s))
        elif s[i] < s[i + 1]:
            print(f"Character at position {i} is less than character at position {i + 1}.")
        else:
            print(f"Character at position {i} is greater than character at position {i + 1}.")

# Example usage
string = "hello"
compare_characters(string)
