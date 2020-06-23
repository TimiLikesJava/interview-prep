class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
            
        i = 0
        j = len(array)-1
        while(j > i):
            if(array[i] != array[j]):
                return False
            i += 1
            j -= 1
        return True
