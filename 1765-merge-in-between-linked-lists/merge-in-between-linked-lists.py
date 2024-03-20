# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = ListNode()
        prev.next = list1
        first = list1
        second = list1.next
        count = 1

        while count != a:
            first = first.next
            second = second.next
            count += 1
        while count != b + 1 and second.next:
            second = second.next
            count += 1
        end = list2
        while end.next:
            end = end.next
        
        first.next = list2
        end.next = second
        return prev.next

