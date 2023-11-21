import tkinter as tk

root = tk.Tk()
root.geometry("1200x700")
label1 = tk.Label(root,text="眠い",font=("Arial", 30))
label2 = tk.Label(root,text="眠い眠い",font=("Arial", 40))
label3 = tk.Label(root,text="眠い眠い眠い",font=("Arial", 50))
label4 = tk.Label(root,text="ねむい!!",font=("Arial", 60))

# label1.pack()

label1.place(x=1100,y=600)

# label1.grid(row=0,column=0)
# label2.grid(row=1,column=1)
# label3.grid(row=0,column=2)
# label4.grid(row=1,column=3)

def button_click():
    text = entry.get()
    print(text)

button = tk.Button(root,text="ボタンだよ",font=("Arial", 30), command=button_click)
button.pack()

entry = tk.Entry(root,font=("Arial",30))
entry.pack()

root.mainloop()


