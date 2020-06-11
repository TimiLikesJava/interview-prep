class Node:
    def __init__(self , data=None , prev = None ,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class dLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def length(self):
        return self.size

    def insert(self , nodeValue):
        newNode = Node(nodeValue)
        if(self.head is None):
            self.head = newNode
            self.tail = self.head
            self.head.next = None
            self.tail.prev = None
            self.size += 1

        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = None
            self.tail = newNode
            self.size += 1

    def insertInBetw(self , prev_node , nodeValue):
        newNode = Node(nodeValue)
        tempNode = prev_node.next
        prev_node.next = newNode
        newNode.next = tempNode
        newNode.prev = prev_node
        tempNode.prev = newNode
        self.size += 1

    def search(self , nodeValue):
        current = self.head
        while(current):
            if(current.data == nodeValue):
                return 'Found!'
            current = current.next
        return 'Not Found!'

    def delete(self , nodeValue):
        current = self.head
        if(self.size == 1):
            self.head = None
            self.tail = None
            self.size -= 1

        if(current.data == nodeValue):
            tempNode = current.next
            current.next = None
            tempNode.prev = None
            self.head = tempNode
            self.size -= 1

        else:
            while(current.next):
                if(current.data == nodeValue):
                    tempNode = current.next
                    current.prev.next = tempNode
                    tempNode.prev = current.prev
                    current.next = None
                    current.prev = None
                    self.size -= 1
                    break
                current = current.next

    def deleteEnd(self):
        current = self.head
        while(current.next):
            current = current.next
        tempNode = current.prev
        tempNode.next = None
        current.prev = None
        self.tail = tempNode
        self.size -= 1


            

        

    def printDLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


LL = dLinkedList()
LL.insert(4)
LL.insert(5)
LL.insert(7)
LL.insertInBetw(LL.head.next , 6)
LL.delete(6)
LL.deleteEnd()
LL.printDLL()


