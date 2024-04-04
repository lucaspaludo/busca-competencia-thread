from tkinter import *
from tkinter import Tk, messagebox
from executa_programa import executaPrograma
from time import sleep
import threading

def disparaThread():
    threading.Timer(15.0, disparaThread).start()
    print('Executando programa')
    executaPrograma()

def telaLogin():
    #cores ------------------------
    co0 = "#f0f3f5"  # preto
    co1 = "#feffff"  # branco
    co2 = "#3fb5a3"  # verde
    co3 = "#38576b"  # valor 
    co4 = "#403d3d"   # letra 

    #criando janela ---------------
    janela = Tk()
    janela.title ('')
    janela.geometry('310x300')
    janela.configure(background=co1)
    janela.resizable(width=FALSE, height=FALSE)

    #dividindo a janela ---------------
    frameCima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
    frameCima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frameBaixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
    frameBaixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    #configurando o frameCima---------------
    lNome = Label(frameCima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
    lNome.place(x=5, y=5)

    lLinha = Label(frameCima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    lLinha.place(x=10, y=45)

    credenciais = ['teste@teste.com', '123456']

    def encerraPrograma():
        if messagebox.askokcancel('Finalizar Programa', 'Tem certea que deseja Finalizar o programa?'):
            janela.destroy()
    #função para autenticar usuário
    def verificaSenha():
        nome = eNome.get()
        senha = ePass.get()

        if credenciais[0] == nome and credenciais[1] == senha:
            janela.after(2000, janela.destroy)
            messagebox.showinfo('Login', 'Seja bem vindo! O programa será iniciado.')
            for widget in frameBaixo.winfo_children():
                widget.destroy()
            for widget in frameCima.winfo_children():
                widget.destroy()
            novaJanela()
            #disparaThread()
            
        else: 
            messagebox.showwarning('Erro', 'Seus dados estão incorretos.')
           
    def novaJanela():
        #configurando o frameCima---------------
        lNome = Label(frameCima, text='Seja bem vindo!', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
        lNome.place(x=5, y=5)

        lLinha = Label(frameBaixo, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
        lLinha.place(x=10, y=45)

    #configurando o frameBaixo---------------
    lNome = Label(frameBaixo, text='E-mail *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    lNome.place(x=10, y=20)
    eNome = Entry(frameBaixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
    eNome.place(x=14, y=50)

    lPass = Label(frameBaixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    lPass.place(x=10, y=95)
    ePass = Entry(frameBaixo, width=25, justify='left', show='*', font=('', 15), highlightthickness=1, relief='solid')
    ePass.place(x=14, y=130)

    bConfirmar = Button(frameBaixo, command=verificaSenha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
    bConfirmar.place(x=15, y=180)

    bEncerrar = Button(frameBaixo, command=encerraPrograma, text='Finalizar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)

    janela.mainloop()

    
