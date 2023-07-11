import tkinter as tk
from tkinter import messagebox

def possible(values, row, col, num):
    for i in range (0,9):
        if values[row][i] == num:
            return False
        elif values[i][col] == num:
            return False
    r0 = 3 * (row // 3)
    c0 = 3 * (col // 3)
    for i in range (0,3):
        for j in range (0,3):
            if values[r0+i][c0+j] == num:
                return False
    return True

def Solve(values, row, col): #recursive function
    if row == 9: #base case
        for i in range(9):
            for j in range(9):
                board[i][j].delete(0, tk.END)
                board[i][j].insert(0, values[i][j])
        return True
    
    if values[row][col] !=0: #moving to next cell
        if col == 8:
            return Solve(values, row+1, 0)
        else:
            return Solve(values, row, col+1)

    if values[row][col] == 0:
        for k in range (1, 10):
            if possible(values, row, col, k):
                    values[row][col] = k
                
                    if col == 8:
                        if Solve(values, row+1, 0):
                            return True
                    else:
                        if Solve(values, row, col+1):
                            return True
                        
                    values[row][col] = 0 #backtracking
                  
    return False

root = tk.Tk()
root.title('Sudoku Solver')
root.geometry("230x300")

# frame to contain the grid
grid_frame = tk.Frame(root)
grid_frame.grid(row=0, column=0)

def get_values(board):
    values = []
    for row in board:
        row_values = []
        for entry in row:
            value = entry.get()
            if value == '':
                row_values.append(0)
            else:
                row_values.append(int(value))
        values.append(row_values)
    return values


# the grid of entry widgets
board = []
for i in range(9):
    row = []
    for j in range(9):
        entry = tk.Entry(grid_frame, width=3)
        entry.grid(row=i, column=j)
        row.append(entry)
    board.append(row)

def RefreshPrg():
    for row in board:
        for entry in row:
            entry.delete(0, tk.END)

def ExitPrg():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


# the solve button
solve_button = tk.Button(root, text='Solve', command=lambda: Solve(get_values(board), 0, 0))
solve_button.grid(row=1, column=0, pady=5)

# the refresh button
refresh_button = tk.Button(root, text='Refresh', command=RefreshPrg)
refresh_button.grid(row=2, column=0, pady=5)

# the exit button
exit_button = tk.Button(root, text='Exit', command=ExitPrg)
exit_button.grid(row=3, column=0, pady=5)

root.mainloop()
