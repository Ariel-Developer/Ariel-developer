import customtkinter as ctk
from validate_email import validate_email as verificando
from hashlib import sha256
from tkinter import messagebox
from tkinter import *
import sqlite3
class sistema:
    def __init__(self):
        """ Este programa é um sistema de Login que irá armarzenar as infomarções (Email & senha) criptografada em um banco de dados
        O sistema ira primeiro criar A tabela para armarzenar (self.criar_banco()), Depois uma interface de cadastro (self.programa_cadastrando())
        e por final a interface de login (self.programa_logando()) que irá analisar se a conta que foi digitada esta dentro do banco de Dados"""

        self.criar_banco()
        self.programa_cadastrando()
        self.programa_logando()
    def criar_banco(self):
        banco = sqlite3.connect("Sistema_de_usuarios.db")
        cursor = banco.cursor()
        cursor.execute('CREATE TABLE informacoes_usuarios (Email, Senha)')
        cursor.close()
        banco.commit()
        banco.commit()
    def programa_cadastrando(self):
        def cadastrar():
            self.email_verificado = verificando(self.email_input.get())
            if self.email_verificado == True and self.senha_input.get().__len__() >=4:
                self.email_codificado = sha256(self.email_input.get().encode()).hexdigest()
                self.senha_codificada = sha256(self.senha_input.get().encode()).hexdigest()

                self.banco = sqlite3.connect('Sistema_de_usuarios.db')
                self.cursor = self.banco.cursor()
                self.cursor.execute(f'INSERT INTO informacoes_usuarios (Email, Senha) VALUES ("{self.email_codificado}", "{self.senha_codificada}")')
                self.cursor.close()
                self.banco.commit()
                self.banco.close()
                self.home_cadastro.destroy()
            elif len(self.email_input.get()) == 0 and len(self.senha_input.get()) == 0:
                messagebox.showerror(title='Error', message='insira as infomarcoes')
            elif len(self.email_input.get()) == 0:
                messagebox.showerror(title='Error', message='insira seu email')
            elif len(self.senha_input.get()) == 0:
                messagebox.showerror(title='Error', message='insira sua Senha')
            elif len(self.senha_input.get()) < 4:
                messagebox.showerror(title='Error', message='A senha deve conter pelo menos 4 caracteres')
                self.senha_input.delete(0, END)
            else:
                messagebox.showinfo(title='Email', message='Este E-mail não é valido!')
                self.email_input.delete(0, END)

        self.home_cadastro = ctk.CTk()
        self.home_cadastro.title("Cadastro")
        self.home_cadastro.resizable(False, False)
        self.home_cadastro.geometry('300x300')
        self.home_cadastro.iconbitmap('favicon (1).ico')
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme('green')


        self.frame_main = ctk.CTkFrame(self.home_cadastro, width=100)
        self.frame_main.pack(pady=22, padx=25, fill='both', expand=True)


        self.label = ctk.CTkLabel(self.frame_main, text='Sistema de Cadastro')
        self.label.pack(pady=20,padx=1)

        self.email_input = ctk.CTkEntry(self.frame_main, placeholder_text='Username', text_font='Helveltica 10 bold', width=200)
        self.email_input.pack(pady=20)

        self.senha_input = ctk.CTkEntry(self.frame_main, placeholder_text="Password", text_font='Helveltica 10 bold', width=200)
        self.senha_input.pack(pady=10)

        self.button = ctk.CTkButton(self.frame_main, text='Cadastrar', text_font='helveltica 10 bold', corner_radius=65, command=cadastrar)
        self.button.pack(pady=20)



        self.home_cadastro.mainloop()
    def programa_logando(self):
        def entrando():
            self.email_login_codificado = sha256(self.email_input_login.get().encode()).hexdigest()
            self.senha_login_codificado = sha256(self.senha_input_login.get().encode()).hexdigest()
            self.banco = sqlite3.connect('Sistema_de_usuarios.db')
            self.cursor = self.banco.cursor()
            self.cursor.execute(f'SELECT * FROM informacoes_usuarios WHERE Email == "{self.email_login_codificado}"')
            self.compativel_email = self.cursor.fetchall()
            self.cursor_senha = self.banco.cursor()
            self.cursor_senha.execute(f'SELECT * FROM informacoes_usuarios WHERE Senha == "{self.senha_login_codificado}"')
            self.compativel_senha = self.cursor_senha.fetchall()

            if len(self.compativel_email) != 0 and len(self.compativel_senha) != 0:
                messagebox.showinfo(title='Entrando', message='Sucesso!')
                self.email_input_login.delete(0, END)
                self.senha_input_login.delete(0, END)
            else:
                messagebox.showerror(title='Not Found', message='Esta conta não existe')


        self.home_login = ctk.CTk()
        self.home_login.title("Login")
        self.home_login.resizable(False, False)
        self.home_login.geometry('300x300')
        self.home_login.iconbitmap('Login-icon.ico')
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme('blue')

        self.frame_main = ctk.CTkFrame(self.home_login, width=100)
        self.frame_main.pack(pady=22, padx=25, fill='both', expand=True)

        self.label = ctk.CTkLabel(self.frame_main, text='Entrando', text_font='Helveltica 11 bold')
        self.label.pack(pady=20)

        self.email_input_login = ctk.CTkEntry(self.frame_main, placeholder_text='Username', text_font='Helveltica 10 bold',
                                        width=200)
        self.email_input_login.pack(pady=20)

        self.senha_input_login = ctk.CTkEntry(self.frame_main, placeholder_text="Password", text_font='Helveltica 10 bold', show='*',
                                        width=200)
        self.senha_input_login.pack(pady=10)

        self.button = ctk.CTkButton(self.frame_main, text='Entrar', text_font='Helveltica 10 bold', corner_radius=80, command=entrando)
        self.button.pack(pady=20)

        self.home_login.mainloop()

working = sistema()

