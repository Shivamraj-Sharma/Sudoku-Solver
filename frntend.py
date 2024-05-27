import tkinter as tk
from tkinter import ttk
from bckend import solver

root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("324x423")

label = tk.Label(root, text="Fill in the numbers and click solve").grid(row=0,column=1,columnspan=10)
errLabel = tk.Label(root,text="",fg="red")
errLabel.grid(row=15,column=1,columnspan=10,pady=5)
solvedLabel = tk.Label(root,text="",fg="green")
solvedLabel.grid(row=15,column=1,columnspan=10,pady=5)

cells = {}

def ValidateNumber(P):
    out = (P.isdigit() or P=="") and len(P)<2 and P!="0"
    return out
reg = root.register(ValidateNumber)

def draw3x3Grid(row,column,bgcolor):
    for i in range(0,3,1):
        for j in range(0,3,1):
            e=tk.Entry(root,width=5,bg=bgcolor,justify="center",font=('calibre',8, 'bold'),validate="key",validatecommand=(reg,"%P"))
            e.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells[(row+i+1,column+j+1)] = e
            

def draw9x9Grid():
    color="#c8bc9c"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo,colNo,color)
            if color=="#c8bc9c":
                color = "#dad2bd"
            else:
                color="#c8bc9c"

def clearValue():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell=cells[(row,col)]
            cell.delete(0,"end")

def getValues():
    board = []
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val= cells[(row,col)].get()
            if val=="":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

btn = ttk.Button(root, command=getValues,text="Solve",width=10)
btn.grid(row=18,column=1,columnspan=5,pady=20)
btn = ttk.Button(root, command=clearValue,text="Clear",width=10)
btn.grid(row=18,column=5,columnspan=5,pady=20)

def updateValues(s):
    sol = solver(s)
    if sol!="No":
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end")
                cells[((rows,col))].insert(0,sol[rows-2][col-1])
        solvedLabel.configure(text="Sudoku Solved!")
    else:
        errLabel.configure(text="No solution exists for this sudoku")

draw9x9Grid()
root.mainloop()