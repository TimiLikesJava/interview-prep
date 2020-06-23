class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2 is not None:
            if(l1.val < l2.val):
                curr.next = l1
                l1 = l1.next
                
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if(l1 is None):
            curr.next = l2
        if(l2 is None):
            curr.next = l1
            
                
            
        return dummy.next
