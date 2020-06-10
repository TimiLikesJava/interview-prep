class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,  nodeValue):
        newNode = Node(nodeValue)
        current = self.head

        if(self.head is None):
            newNode.next = current
            self.head = newNode

        
        else:
            while(current.next):
                current = current.next
            current.next = newNode
            newNode.next = None

    def insertIB(self , prev_node , nodeValue):
        newNode = Node(nodeValue)
        newNode.next = prev_node.next
        prev_node.next = newNode

    def printLL(self):
        current = self.head
        while(current): #Traversal
            print(current.data)
            current = current.next

    def search(self , nodeValue):
        current = self.head
        while(current):
            if(current.data == nodeValue):
                return 'Found!'
            current = current.next
        return 'Not found!'

    def delete(self , nodeValue):
        current = self.head

        if(current.data == nodeValue):
            self.head= current.next
            current = None

        while(current):
            if(current.data == nodeValue):
                break
            prev = current
            current = current.next

        if(current == None):
            return

        prev.next = current.next
        current = None

    def deleteLL(self):
        self.head = None
        print('Deleted!')

   


        
LL = LinkedList()
LL.insert(5)
LL.insert(6)
LL.insert(8)
LL.insertIB(LL.head.next, 7)
LL.printLL()
LL.delete(7)
print(LL.search(3))
print()
LL.printLL()
print()
LL.deleteLL()
LL.printLL()
