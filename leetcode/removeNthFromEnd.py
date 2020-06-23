class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        for i in range(1 , n+2):
            fast = fast.next
            
        while(fast is not None):
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        return dummy.next
