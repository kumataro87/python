import tkinter
from tkinter import messagebox

def button_click():
    input_value = input_box.get()
    messagebox.showinfo('クリックイベント',input_value + 'が入力されました')

root = tkinter.Tk()
root.title('Python GUI')
root.geometry('360x240')

#入力蘭の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=100)

input_label =tkinter.Label(text="ラベル")
input_label.place(x=10,y=70)

button = tkinter.Button(text='実行ボタン', command=button_click)
button.place(x=10, y=130)

#ウィンドウの描画
root.mainloop()