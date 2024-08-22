# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_current = l1
        l2_current = l2
        carry = 0
        while l2_current.next != None:
            x = l1_current.val + l2_current.val + carry
            l1_current.val = x % 10
            carry = x // 10

            l2_current = l2_current.next
            if l1_current.next != None:
                l1_current = l1_current.next
            else:
                l1_current.next = ListNode()
                l1_current = l1_current.next

        x = l1_current.val + l2_current.val + carry
        l1_current.val = x % 10
        carry = x // 10

        while carry:
            if l1_current.next != None:
                l1_current = l1_current.next
            else:
                l1_current.next = ListNode()
                l1_current = l1_current.next
                
            x = l1_current.val + 1
            l1_current.val = x % 10
            carry = x // 10

        return l1
