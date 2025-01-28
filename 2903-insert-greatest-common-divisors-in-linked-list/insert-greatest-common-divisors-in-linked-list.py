# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = head
        curr = head.next

        if not curr:
            return head

        while curr:
            newNode = ListNode(math.gcd(prev.val, curr.val), curr)
            prev.next = newNode
            prev = curr
            curr = curr.next
        
        return dummy.next