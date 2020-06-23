class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head is None):
            return
        odd = head
        even = head.next
        evenHead = even
        
        while even and even.next!=None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
