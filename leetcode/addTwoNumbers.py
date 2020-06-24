class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2:
            if(l1 is not None):
                x = l1.val
            else:
                x = 0
            if(l2 is not None):
                y = l2.val
            else:
                y = 0
                
            c_sum = x + y + carry
            curr.next = ListNode((c_sum) % 10)
            carry = c_sum // 10
            
            if(l1 is not None):
                l1 = l1.next
            if(l2 is not None):
                l2 = l2.next
            curr = curr.next
        if(carry > 0):
            newNode = ListNode(carry)
            curr.next = newNode
            
            
        
        return dummy.next
