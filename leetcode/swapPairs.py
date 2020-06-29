class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next is not None:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            curr.next = second
            curr.next.next = first
            
            curr = curr.next.next
            
        return dummy.next
