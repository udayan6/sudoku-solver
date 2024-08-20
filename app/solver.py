def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])): #board is saved as a 2d list
            if bo[i][j] == 0:
                return (i,j) #row, col
            
def valid(bo, num, pos):

    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    #Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #Check box
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(bo): #utilises a backtracking algorithm to solve the board
    find = find_empty(bo)
    if not find:
        return bo #if it's already solved return the board (base case)
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            result = solve(bo) #recursive call/rescursive case
            if result:
                return result
                
            
            bo[row][col] = 0

    return None