class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        mem = set()
        while(headA):
            mem.add(headA)
            headA = headA.next
            
            
        while(headB):
            if(headB in mem):
                return headB
            headB = headB.next
