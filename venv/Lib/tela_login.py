from tkinter import *
from tkinter import Tk, messagebox
from executa_programa import executaPrograma
from time import sleep
import subprocess
import win32serviceutil
import win32event
import win32service


class ServicoDeTeste(win32serviceutil.ServiceFramework):
    _svc_name_ = "robobuscacompetenci1a"
    _svc_display_name_ = "Serviço competencia1"
    _svc_description_ = "O serviço irá verificar uma rota em busca de arquivos para serem organizados."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hwaitStop = win32event.CreateEvent(None, 0, 0, None)

    def svcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hwaiStop)
    
    def SvcDoRun(self):
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

        executaPrograma()
        sleep(15)
        
        
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

    def checkServiceExists(service_name):
        try:
            subprocess.run(['sc', 'query', service_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def startService(service_name):
        try:
            subprocess.run(['sc', 'start', service_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f'O serviço {service_name} foi iniciado com sucesso.')
        except subprocess.CalledProcessError as e:
            print(f'Erro ao iniciar o serviço {service_name}: {e.stderr.decode().strip()}')


    #função para autenticar usuário
    def verificaSenha():
        nome = eNome.get()
        senha = ePass.get()

        if credenciais[0] == nome and credenciais[1] == senha:
            janela.after(2000, janela.destroy)
            messagebox.showinfo('Login', 'Seja bem vindo! Seu serviço será iniciado...')

            #win32serviceutil.RemoveService(ServicoDeTeste._svc_name_)
           
            if checkServiceExists(ServicoDeTeste._svc_name_):
                print(f'O serviço {ServicoDeTeste._svc_name_} existe.')
                startService(ServicoDeTeste._svc_name_)
            else:
                print(f'O serviço {ServicoDeTeste._svc_name_} não existe.')
                win32serviceutil.InstallService('ServicoDeTeste', ServicoDeTeste._svc_name_, ServicoDeTeste._svc_display_name_, startType=win32service.SERVICE_AUTO_START, bRunInteractive=1, exeName=r'C:\Python312\pythonservice.exe', description=ServicoDeTeste._svc_description_)
                print(f'Serviço {ServicoDeTeste._svc_name_} instalado com sucesso.')
                startService(ServicoDeTeste._svc_name_)
            
        else: 
            messagebox.showwarning('Erro', 'Seus dados estão incorretos.')
           

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

    janela.mainloop()
    
