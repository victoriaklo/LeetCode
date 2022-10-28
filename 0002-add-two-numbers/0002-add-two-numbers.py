# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # var to track carry over num if num is summeed > 10. carry = val // 10
        #remainder = % 10
    
        result_llist = ListNode()
        curr = result_llist
        carry = 0
        
        while l1 or l2 or carry:
            total = 0
            
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if carry:
                total += carry
            
            carry = total //10
            remainder = total % 10
            
            curr.next =ListNode(remainder)
            curr = curr.next
        
        return result_llist.next

            
            
            
        
        