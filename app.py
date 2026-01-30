
import streamlit as st

# import tkinter as tk
# from tkinter import ttk


#def click_btn():
#    button["text]="予想結果"

# root =tk.Tk()
# root.title("うま王")
# root.geometry("1300x800")

st.title("うま王")


canvas=st.Canvas(root,width=1300,height=100,bg="Sky Blue")
#canvas.place(x=0,y=0)
canvas.pack()
canvas=st.Canvas(root,width=1300,height=700,bg="brown")
#canvas.place(x=500,y=500)
canvas.pack()


label = st.Label(root,text="うま王2026",font=("BIZ UDPゴシック",24))
label.place(x=50,y=50)

#button=tk.Button(root,text="予想表示",font=("BIZ UDPゴシック",16))
#button.place(x=1100,y=50)


def select_combo(event):
    #print(combobox.get())
    # 予想画像表示
    enemy=combobox.get()
    match enemy:

        case "京成杯":
           print(enemy)
           gazou=st.PhotoImage(file="0118京成杯.png")
           canvas.create_image(650,280,image=gazou)
        case "日経新春杯":
           print(enemy)
           gazou=st.PhotoImage(file="0118日経新春杯.png")
           canvas.create_image(650,280,image=gazou)        
        case "フェアリーＳ":
           print(enemy)
           gazou=st.PhotoImage(file="0111フェアリーS.png")
           canvas.create_image(650,280,image=gazou)
        case "シンザン記念":
           print(enemy)
           gazou=st.PhotoImage(file="0112シンザン記念.png")
           canvas.create_image(650,280,image=gazou)
        case "中山金杯":
           print(enemy)
           gazou=st.PhotoImage(file="0104中山金杯.png")
           canvas.create_image(650,280,image=gazou)
        case "京都金杯":
           print(enemy)
           gazou=st.PhotoImage(file="0104京都金杯.png")
           canvas.create_image(650,280,image=gazou)
        
    canvas.pack()  
    canvas.create_image(650,280,image=st.PhotoImage(file=enemy+".png"))
    canvas.pack(padx=10, pady=10)
           
# 選択肢と変数
options=["京成杯","日経新春杯","フェアリーＳ", "シンザン記念","中山金杯","京都金杯"]
v=st.StringVar()

# 選択された値を表示する関数
v=tk.StringVar()
combobox  = ttk.Combobox(root,values=options,height=10,
textvariable=v,font=("BIZ UDPゴシック",16,"bold"))
combobox.bind('<<ComboboxSelected>>',select_combo)
combobox.pack(padx=200, pady=50)
combobox.place(x=350,y=50)







root.mainloop()

