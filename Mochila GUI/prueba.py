from tkinter import *

a=("a","b","c","d","e","1","2","3","f","4","5","6","g","7","8","9")
s=0
root = Tk()

# for r in range(0,4):
#     for c in range(0,4):
#         b=a[s]
#         s+=1
#         celda = Label(root,text=b, width=8)
#         celda.grid(padx=5, pady=5, row=r, column=c)
#         celda.config(fg="white",    # Foreground
#              bg="skyblue",   # Background
#              font=("Verdana",12))

for r in range(0, 8):
    for c in range(0, 3):
        celda = Entry(root, width=8)
        celda.grid(padx=5, pady=5, row=r, column=c)
        celda.insert(0, '({}, {})'.format(r, c))
        celda.config(fg="white",    # Foreground
                    bg="skyblue",   # Background
                    font=("Verdana",12))

root.mainloop()

