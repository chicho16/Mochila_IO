from tkinter import *

class Main_screen(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.grid()
        self.text = Label(text="Janela")
        self.text.grid()
        root.withdraw()
        self.create_login()

    def create_login(self):
        self.root2 = Toplevel()
        self.app2 = Login_screen(self.root2)

class Login_screen(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.botao1 = Button(self,text="Appear",command = lambda: self.show_main())
        self.botao1.grid()

    def show_main(self):
        self.master.destroy()
        root.deiconify()


root = Tk()
app = Main_screen(root)
root.mainloop()