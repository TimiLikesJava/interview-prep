class Node:
    def __init__(self , data=None , next =None):
        self.data = data
        self.next = next

class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def insert(self , nodeValue):
        current = self.head
        newNode = Node(nodeValue)
        if(current is None):
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = self.head

    def insertIB(self , prev_node , nodeValue):
        newNode = Node(nodeValue)
        newNode.next = prev_node.next
        prev_node.next = newNode


    def delete(self , nodeValue):
        if (self.head.next is self.head):
            self.head = None
            self.tail = None

        if(self.head.data == nodeValue):
            self.head = self.head.next
            self.tail.next = self.head

        else:
            current = self.head
            prev = None
            while(current.next != self.head):
                if(current.data == nodeValue):
                    prev.next = current.next
                prev = current
                current = current.next

            if(current == self.tail):
                current = self.head
                while(current.next != self.tail):
                    current = current.next
                current.next = self.head
    

    def printCLL(self):
        current = self.head
        while(current):
            if(current.next == self.head):
                print(current.data)
                break
            print(current.data)
            current = current.next

    


LL = CLinkedList()
LL.insert(4)
LL.insert(5)
LL.insert(7)
LL.insertIB(LL.head.next , 6)
LL.delete(7)
LL.printCLL()




