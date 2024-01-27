# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summary: list[int] = []
        carry = 0

        while l1 is not None or l2 is not None:
            sum_position = 0

            if l1 is not None:
                sum_position += l1.val
                l1 = l1.next

            if l2 is not None:
                sum_position += l2.val
                l2 = l2.next

            summary.append((sum_position + carry) % 10)

            if sum_position + carry > 9:
                carry = (sum_position + carry) // 10
            else:
                carry = 0
    
        if carry != 0:
            summary.append(carry)

        previous = None
        head = None
        for i in range(len(summary)):
            node = ListNode(summary[i])

            if previous is None:
                head = node
                previous = node
                continue
        
            previous.next = node
            previous = node
        
        return head