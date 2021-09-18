#Importando bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import banco

#Criação da Janela
tela = Tk()
tela.title("Login")
tela.geometry("600x300")
tela.configure(background="white")
tela.resizable(width=False, height=False)
tela.iconbitmap(default="loginPython\imagens\LogoIcon.ico")

#Carregando Imagens
logo = PhotoImage(file="loginPython\imagens\logo.png")

#Widgets
LeftFrame = Frame(tela, width=200, height=300, bg="midnightblue", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(tela, width=395, height=300, bg="midnightblue", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="midnightblue")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Usuário: ", font=("Century Gothic", 20), bg="midnightblue", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Senha: ", font=("Century Gothic", 20), bg="midnightblue", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

def Login():
    Usuario = UserEntry.get()
    Senha = PassEntry.get()

    banco.cursor.execute("""
    SELECT * FROM Usuarios WHERE (Usuario = ? AND Senha = ?)
    """, (Usuario, Senha))
    print("Conectado")
    VerificarLogin = banco.cursor.fetchone()
    try:
        if (Usuario in VerificarLogin and Senha in VerificarLogin):
            messagebox.showinfo(title="Login info", message="Acesso Confirmado")
    except:
        messagebox.showinfo(title="Login info", message="Usuário/Senha incorreto ou não cadastrado")

#Botoes
loginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
loginButton.place(x=100, y=225)

def Cadastrar():
    #Removendo os Widgets de Login
    loginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo os de Cadastro
    NomeLabel = Label(RightFrame, text="Nome: ", font=("Century Gothic", 20), bg="midnightblue", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame,width=30)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email: ", font=("Century Gothic", 20), bg="midnightblue", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=100, y=66)

    def CadastrarBanco():
        Nome = NomeEntry.get()
        Email = EmailEntry.get()
        Usuario = UserEntry.get()
        Senha = PassEntry.get()

        if(Email == "" and Nome == "" and Usuario == "" and Senha == ""):
            messagebox.showerror(title="Register Erro", message="Preencha todos os campos!")
        else:
            banco.cursor.execute("""
                INSERT INTO Usuarios(Nome, Email, Usuario, Senha) VALUES (?, ?, ?, ?)
            """, (Nome, Email, Usuario, Senha))
            banco.conn.commit()
            messagebox.showinfo(title="Register Info", message="Cadastrado com sucesso!")

    Register = ttk.Button(RightFrame, text="Cadastrar", width=30, command=CadastrarBanco)
    Register.place(x=100, y=225)

    def VoltarLogin():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        loginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Voltar", width=20, command=VoltarLogin)
    Back.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="Cadastrar", width=20, command=Cadastrar)
RegisterButton.place(x=125, y=260)

tela.mainloop()
