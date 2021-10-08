from tkinter import *
from math import *
from tkinter import messagebox
#create the main window
root=Tk()
root.title("Calculator V1.1")
root.iconbitmap("calculator.ico")
root.geometry("500x950")
# root.Font(size=20)
frame_input=Frame(root, padx=10,pady=10,border=5)
frame_input.pack(padx=10,pady=10)
global my_input
def press(x):
    my_input=entry_input.get()+str(x)
    entry_input.delete(0, END)
    entry_input.insert(0, my_input)
n=5

def calc():
    try:
        global ans
        ans=round(eval(entry_input.get().replace("^","**")),n)
        label_result.configure(text=str(ans))
    except:
        label_result.configure(text="Error !")
def clear():
    entry_input.delete(0, END)
    label_result.configure(text="")

def ans():
    entry_input.delete(0, END)
    entry_input.insert(0,str(ans))
    label_result.configure(text="")
def sq_rt():
    x=entry_input.get()
    entry_input.delete(0, END)
    entry_input.insert(0, "sqrt("+ str(round(eval(x),n))+")")
    label_result.configure(text=round(eval(str(sqrt(eval(x)))),n))




#create input screen
entry_input=Entry(frame_input,border=4,width=25,font=("Courier",28,'bold'))
entry_input.grid(row=0,column=0,columnspan=4)
label_result=Label(frame_input,border=4,width=25,text="0",font=("Courier",28,'bold'))
label_result.grid(row=1,column=0,columnspan=4)

#create frame for buttons
frame_buttons=Frame(root)
frame_buttons.pack()

buttons=[i for i in range(1,10)]+[0,'-','+','*','.','/']
for i in range(15):
    buttons[i]=Button(frame_buttons,text=str(buttons[i]),height = 2, width = 2,padx=2,pady=4,command =lambda x=buttons[i]:press(x),font=("Courier",28,'bold'))
    buttons[i].grid(row=(i//3),column=(i%3))

Button(frame_buttons,text="Enter",command=calc,height = 6, width = 6,font=("Courier",28,'bold'),padx=5,pady=5).grid(row=0,column=4,rowspan=2)
Button(frame_buttons,text="Clear",command=clear,height = 2, width = 6,font=("Courier",28,'bold'),padx=5,pady=5).grid(row=2,column=4)
Button(frame_buttons,text="sqrt",command=sq_rt,height = 2, width = 6,font=("Courier",28,'bold'),padx=5,pady=5).grid(row=3,column=4)
Button(frame_buttons,text="Ans.",command=ans,height = 2, width = 6,font=("Courier",28,'bold'),padx=5,pady=5).grid(row=4,column=4)

root.bind('<Return>',lambda x=0:calc())

root.mainloop()
