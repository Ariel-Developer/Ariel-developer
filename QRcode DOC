from tkinter import *
import qrcode
def qrcode1(event):
    root.geometry("500x400")
    qr = qrcode.make(entry.get())
    qr.save("qrcodeYT.jpg")
    entry.destroy()
    pht = PhotoImage(file="qrcodeYT.jpg")
    label = Label(image=pht)
    label.pack()

root = Tk()
root.geometry("300x100")
co = Label(root, text='Coloque o Link aqui')
co.place(x=50, y=25)
entry = Entry()
entry.place(x=50, y=50, width=180)
entry.bind("<Return>", qrcode1)
root.mainloop()



