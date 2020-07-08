class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.array = [0] * k
        self.start = self.top = -1
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if(self.isFull()):
            return False
        else:
            if(self.top + 1 == len(self.array) and self.start != 0):
                self.top = 0
                self.array[self.top] = value
                return True
            else:
                if(self.isEmpty()):
                    self.start += 1
                    self.top += 1
                    self.array[self.start] = value
                    return True
                else:
                    self.top += 1
                    self.array[self.top] = value
                    return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        
        if(self.isEmpty()):
            return False
        else:
            if(self.start == self.top):
                self.start = self.top = -1
                return True
            if(self.start + 1 == len(self.array)):
                self.start = 0
                return True
                
            else:
                self.start += 1
                return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if(self.isEmpty()):
            return -1
        else:
            return self.array[self.start]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if(self.isEmpty()):
            return -1
        else:    
            return self.array[self.top]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if(self.start == -1):
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if(self.top + 1 == self.start):
            return True
        elif(self.top + 1 == len(self.array) and self.start == 0):
            return True
        else:
            return False
