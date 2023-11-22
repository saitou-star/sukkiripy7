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

# 画像を表示    
load_image = tk.PhotoImage(file="curry.png") # 画像読み込み
img = tk.Label(root, image=load_image) # 表示するために画像を渡す⇒imgに
img.pack() # 画像を配置(= pack())


# 複数行のメッセージ
msg = tk.Message(
    root,
    text="ああああ眠い！！！ぐあああああああああああああああああああああ", # テキスト
    font=('Arial', 20), # 文字の種類,大きさ
    bg = "white", # バックグラウンドの色
    width = 300 # テキスト表示のウインドウの大きさ
)
# msg.pack()

# canvasを使う
canvas = tk.Canvas(root, bg="pink", width=500,height=300) # canvasウインドウ ＆ バックグラウンドのピンク ＆ サイズ
canvas.pack() # 配置
# ↓の20,20=x軸,y軸だが、textの真ん中が0，0の位置になる。fillは塗りつぶす。anchorで基準値が左上になる(n=north,w=west,c=center(真ん中))
canvas.create_text(0, 0, text="キャンパスもりもり", fill='white', font=("Arial", 20),anchor='nw') 
canvas.create_text(float(canvas["width"])/2, float(canvas["height"])/2, text="えっ、なんで？", fill='white', font=("Arial", 20),anchor='center') 
canvas.create_text(canvas["width"], canvas["height"], text="しゃべっていい？", fill='white', font=("Arial", 20),anchor='se') 


root.mainloop()


