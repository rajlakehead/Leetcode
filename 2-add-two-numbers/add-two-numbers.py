# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = ListNode()
        head = prev

        while l1 or l2:
            v1, v2 = 0, 0

            if l1: v1 = l1.val
            if l2: v2 = l2.val

            val = v1 + v2 + carry
            newnode = ListNode(val % 10)
            carry = val // 10
            head.next = newnode
            head = head.next
            
            if l1: l1= l1.next
            if l2: l2 = l2.next

        if carry:
            newnode = ListNode(carry)
            head.next = newnode
        return prev.next
            

        