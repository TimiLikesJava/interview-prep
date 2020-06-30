def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(head is None):
            return
        if(k == 0):
            return head
        count = 0
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        if(count == 1):
            return head
        if(count == k):
            return head
        num = count - (k % count)
        num = num - 1
        
        point = head
        for i in range(num):
            point = point.next
        temp = point.next
        if(temp is None):
            return head
        point.next = None
        if(temp.next is None):
            temp.next = head
            head = temp
            return head
        else:
            ans = temp
            while ans.next is not None:
                ans = ans.next
            ans.next = head
            head = temp
            return head
