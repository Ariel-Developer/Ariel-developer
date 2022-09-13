from tkinter import *
import sqlite3
import pandas as pd
def janelas():
    def cadastrar_clientes():
        banco = sqlite3.connect("tabela")
        cursor = banco.cursor()
        cursor.execute("INSERT INTO cliente VALUES (:nome, :sobrenome, :email, :telefone)",
                       {
                           'nome': entry01.get(),
                           "sobrenome": entry02.get(),
                           "email": entry03.get(),
                           "telefone": entry04.get()
                       }
                       )
        banco.commit()
        banco.close()
        entry01.delete(0, END)
        entry02.delete(0, END)
        entry03.delete(0, END)
        entry04.delete(0, END)
    def exporta_clietes():
        banco = sqlite3.connect('tabela')

        cursor = banco.cursor()
        cursor.execute("SELECT *, oid FROM cliente")
        clientes_cadastrados = cursor.fetchall()
        clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns={'nome', 'sobrenome', 'email', 'telefone', 'id_banco'})
        clientes_cadastrados.to_excel("banco_clientes.xlsx")
        banco.commit()
        banco.close()


    janela = Tk()
    janela.geometry("250x260")
    janela.resizable(False, False)
    janela.title("Cadastro")


    #Projeto principal

    name = Label(janela, text="Nome")
    name.place(x=20, y=10)

    entry01 = Entry(janela)
    entry01.place(x=70, y=12, width=170)

    second_name = Label(janela, text="Sobrenome")
    second_name.place(x=3, y=40)

    entry02 = Entry(janela)
    entry02.place(x=70, y=42, width=170)

    email = Label(janela, text="E-mail")
    email.place(x=19, y=70)

    entry03 = Entry(janela)
    entry03.place(x=70, y=72, width=170)


    telefone = Label(janela, text="Telefone")
    telefone.place(x=12, y=100)

    entry04 = Entry(janela)
    entry04.place(x=70, y=102, width=170)

    button01 = Button(janela, text="Cadastrar Cliente", activebackground="yellow", command=cadastrar_clientes)
    button01.place(x=70, y=150)

    button02 = Button(janela, text="Exportar Base de Clientes", activebackground="yellow",command=exporta_clietes)
    button02.place(x=50, y=190)




    janela.mainloop()
janelas()