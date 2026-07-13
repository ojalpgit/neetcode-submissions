"""
UMPIRE- 

Understand- 
1. Input - 9x9 grid "board" 2d arrays of strings
2. Output - true or false 

Map- 
Sets because each element only occurs once in a set 

Implement- 
1. for each row:
    - convert the row into set 
    - add all the elements of the row 
    - subtract the set from the addition 
    - if the difference is greater than 0 then an element has been repeated 
2. repeat this step for column 
3. repeat this step of 3x3 boxes inside of the grid 

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for each row calculation
        for row in board:
            list_row = []
            for i in row:
                if i != ".":
                    list_row.append(int(i))
            set_row = set(list_row)
            set_sum = sum(set_row)
            list_sum = sum(list_row)
            if list_sum - set_sum > 0:
                return False 
        
        #for each column calculation 
        for i in range(9):
            list_col = []
            for row in board:
                if row[i] != ".":
                    list_col.append(int(row[i]))
            set_col = set(list_col)
            set_sum = sum(set_col)
            list_sum = sum(list_col)
            if list_sum - set_sum > 0:
                return False

        start_i = 0
        end_i = 3
        for a in range(3):
            start_j = 0
            end_j = 3
            for b in range(3):
                list_square = []
                for i in range(start_i, end_i):
                    for j in range(start_j, end_j):
                        if board[i][j] != ".":
                            list_square.append(int(board[i][j]))
                set_square = set(list_square)
                set_sum = sum(set_square)
                list_sum = sum(list_square)
                if list_sum - set_sum > 0:
                    return False
                start_j = start_j + 3 
                end_j = end_j + 3
            start_i = start_i + 3 
            end_i = end_i + 3

        return True 


        