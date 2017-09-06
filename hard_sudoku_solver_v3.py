# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 11:41:48 2017

@author: eria
"""

def solve(board):
    import time
    import numpy as np
    
    rows = 9
    cols = 9
    

    solve_sequence = [(row, col) for row in range(rows) for col in range(cols)]
    
# find the first unknown position in the solve_sequence
    first_zero = 0
    row, col = solve_sequence[first_zero]
    while board[row][col] != 0:
        first_zero += 1
        row, col = solve_sequence[first_zero]
        
# find the last unknown position in solve_sequence
    last_zero = len(solve_sequence) - 1
    row, col = solve_sequence[last_zero]
    while board[row][col] != 0:
        last_zero -= 1
        row, col = solve_sequence[last_zero]
    
    def get_possibilities(row, col, board):
        board = np.array(board)
        possible = [x for x in range(1,10)]
        box = board[3*(row//3):3*(row//3)+3, 3*(col//3):3*(col//3)+3]
        not_possible = set()
        for val in possible:
            if val in board[row,:] or val in board[:,col] or val in box:
                not_possible.add(val)
        for num in not_possible:
            possible.remove(num)
        print('row: ', row, 'col: ', col, 'possible', possible, 'box:', box)
        return(possible)
    
    def is_allowed(board, row, col, guess):
        if guess in get_possibilities(row, col, board):
            allowed = True
        else:
            allowed = False
        return(allowed)
        
    def get_next_zero(board, solve_seq_index):
        next_zero_index = solve_seq_index +1
        while next_zero_index < len(solve_sequence) - 1:
            nxt_row, nxt_col = solve_sequence[next_zero_index]
            if board[nxt_row][nxt_col] == 0:
                return(next_zero_index)
            else:
                next_zero_index += 1
        return(next_zero_index)
            
    def try_one_to_nine(board, solve_seq_index, solved):
        if solved:
            return(board, solved)
        row, col = solve_sequence[solve_seq_index]
        for guess in range(1,10):
            print('Checking row: ', row, 'col: ', col, ' = ', guess)
            #time.sleep(1)
            if is_allowed(board, row, col, guess):
                print("OK")
                board[row][col] = guess
                for line in board:
                    print(line)
                print('-' * 40)
                print('last zero =', last_zero)
                print('solve_seq_index =', solve_seq_index)
                if solve_seq_index == last_zero:
                    print('done ... last zero =', last_zero)
                    print('solve_seq_index =', solve_seq_index)
                    solved = True
                    return(board, solved)
                else:
                    board, solved = try_one_to_nine(board, get_next_zero(board, solve_seq_index), solved)
            else:
                if guess == 9:
                    board[row][col] = 0
                    return(board, solved)
    
    solved = False          
    answer, _ = try_one_to_nine(board, first_zero, solved)
    return(answer)    
            
            
            
            
            
            
            
            
            
            
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

puzzle2 = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

puzzle3 = [[4, 5, 0, 3, 9, 1, 8, 7, 6], 
                                  [3, 1, 0, 6, 7, 5, 2, 9, 4], 
                                  [6, 7, 0, 4, 2, 8, 3, 1, 5], 
                                  [8, 3, 0, 5, 6, 4, 7, 2, 9], 
                                  [2, 4, 0, 9, 8, 7, 1, 6, 3], 
                                  [9, 6, 0, 2, 1, 3, 5, 4, 8], 
                                  [7, 9, 0, 8, 5, 2, 4, 3, 1], 
                                  [1, 8, 0, 7, 4, 9, 6, 5, 2], 
                                  [5, 2, 0, 1, 3, 6, 9, 8, 7]]