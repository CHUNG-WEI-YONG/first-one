from tkinter import *

root = Tk()
root.title("Second Large Number")
input_num = StringVar()
v= []

Label(root,text = "Enter your number:").grid(row = 0 ,column = 0)
a = Entry(root , width = 10,textvariable = input_num)
a.grid(row = 0 ,column =1)


Show= Text(root,state = "disabled",width=10,height=1)
Show.grid(row = 2, column =0 ,padx = 20)
Result= Text(root,state = "disabled",width=10,height=1)
Result.grid(row = 3, column =0 ,padx = 20)



def save():
    try:
        e=int(input_num.get())
        input_num.set("")
        if e not in v:
                    v.append(e)
        v.sort(reverse = True)
        Show.config(state = "normal")
        Show.insert(END,v)
        Show.delete("1.0", END)# 清空旧内容
        Show.insert(END, f"{v}\n")
        Show.config(state = "disabled")
    except ValueError:
        print("Please enter a number")
        input_num.set("")

def shown():
    Result.config(state = "normal")
    if len(v)< 3:
        Result.delete("1.0",END)
        Result.insert(END , "No enough words")
    else:
        Result.delete("1.0",END)
        Result.insert(END,f"{v[1]}")
    Result.config(state = "disabled")
        
Button(root,text = "Save number",fg = "green",command = save)\
                 .grid(row = 1, column =0,padx = 10)
Button(root,text = "Show number",fg = "red",command = shown)\
                 .grid(row = 1, column =1,padx = 10)





mainloop()

