class Solution:
    def totalNQueens(self, n: int) -> int:
        res = [] # where we will store results
        col_space = [] # This space is for the columns, but will contain what row number the queen will be on
        self.solveNQueens(n , 0 , col_space , res)
        return len(res) # returns the length of the result
    def solveNQueens(self, n , row , col_space , res):
        if(n == row): # Base case meaning all our choices have been met
            res.append(col_space)
            return
            
        for i in range(0 , n):
            col_space.append(i) # We will start by putting the first element
            if(self.isValid(col_space)): # If this comes out to be true, we can advance to the next column as we search for the next row and the cell where the queen can be placed
                self.solveNQueens(n , row+1 , col_space , res)
            col_space.pop() # If it happens to fail, we have to backtrack and use the next index
            
            
    def isValid(self , col_space):
        row = len(col_space) - 1 # This indicates the row we are in
        
        for i in range(0 , row):
            col_no = abs(col_space[i] - col_space[row]) # This is the column difference for the respective rows. If we use [0,0] for example, the col_no will be zero. This is because on the previous row a queen is placed on the 0th column and this current queen is on the 1st row. This means they are on the same column.
            
            row_no = row - i # This is the row difference
            
            if col_no == 0 or col_no == row_no: # 'col_no == row_no' handles our diagonal case. In a case of [0 , 1] we have the col_no to be 1 and the row_no as well. To visualize this I will use a 4x4 chess board.   Q . . .
            #  . Q . . 
            # As you can see, this is a digonal attack and the queen on the first row is not safe.
                
                return False
            
        return True # We ultimately have to find all safe choices in order for this algorithm to give us the correct output.
