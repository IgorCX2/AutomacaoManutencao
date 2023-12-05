#app_funcition
import time
from datetime import datetime

def reiniciar_temporizador(app, event):
    app.tempo_inativo = time.time()

def verificar_inatividade(app):
    app.after(1000, lambda: verificar_inatividade(app))
    if time.time() - app.tempo_inativo > 5:
        if(app.pagina_ativa == "decanso"):
            return 0
        app.mostrar_pagina_descanso(True)
        return 0
    elif app.pagina_ativa != "decanso":
        return 0
    else:
        app.mostrar_pagina_principal()
        return 0
    
def mostrar_pagina_principal(app):
    app.title("Sistema Manutenção")
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
    app.frame_descanso.pack_forget()
    app.frame_adm.pack_forget()
    app.frame_login.pack_forget()
    app.frame_pcf.pack_forget()
    app.frame_lotto.pack_forget()
    app.frame_aprovarlotto.pack_forget()
    app.frame_principal.pack()

def mostrar_pagina_descanso(app, acao):
    app.title("Tela em Construção")
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
    app.frame_adm.pack_forget()
    app.frame_pcf.pack_forget()
    app.frame_login.pack_forget()
    app.frame_lotto.pack_forget()
    app.frame_principal.pack_forget()
    app.frame_aprovarlotto.pack_forget()
    app.frame_descanso.pack()


#app
import customtkinter
from app_functions import *

from frame_principal import FramePrincipal
from frame_descanso import FrameDescanso
from frame_lotto import FrameLotto
from frame_pcf import FramePcf
from frame_adm import FrameAdm
from frame_login import FrameAdmLogin
from frame_aprovarlotto import FrameAprovaLotto

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Aplicativo(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)
        self.pagina_ativa = None
        button_inicio = customtkinter.CTkButton(self, text="Página Inicial", font=("Helvetica", 12), fg_color='transparent', text_color='white', command=self.mostrar_pagina_principal)
        button_inicio.place(x=0, y=0)
        button_msg = customtkinter.CTkButton(self, text="Em Desenvolvimento", font=("Helvetica", 12), fg_color='transparent', text_color='white')
        button_msg.place(x=145, y=0)
        button_adm = customtkinter.CTkButton(self, text="ADM", font=("Helvetica", 12), fg_color='transparent', text_color='white', command=self.mostrar_pagina_login)
        button_adm.place(x=self.winfo_screenwidth()-150, y=0) 
        self.tempo_inativo = 0
        self.bind("<Motion>", lambda event: reiniciar_temporizador(self, event))

        self.frame_principal = FramePrincipal(self)
        self.frame_descanso = FrameDescanso(self)
        
        #Adc caminho das novas paginas
        self.paginas = {
            "principal": self.mostrar_pagina_principal,
            "descanso": self.mostrar_pagina_descanso,
        }
        self.mostrar_pagina_principal()

    def verificar_inatividade(self):
        self.after(1000, lambda: verificar_inatividade(self))

    #Adc caminho das novas paginas
    def mostrar_pagina_principal(self):
        self.pagina_ativa = "principal"
        mostrar_pagina_principal(self)


    def mostrar_pagina_descanso(self, acao):
        self.pagina_ativa = "decanso"
        mostrar_pagina_descanso(self, acao)

if __name__ == "__main__":
    app = Aplicativo()
    app.verificar_inatividade()
    app.mainloop()

#frame_descanso
import customtkinter
from datetime import datetime
class FrameDescanso(customtkinter.CTkFrame):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(self, master)
        self.master = master
        self.label = customtkinter.CTkLabel(self, text="Pensando em algo incrível =)")
        self.label.pack(pady=20)

        self.horario_label = customtkinter.CTkLabel(self, text="HORARIO", font=("Helvetica", 60, "bold"), fg_color='transparent', text_color='white')
        self.horario_label.pack(pady=50)

        self.teste()

    def teste(self):
        print("verificar")
        data_atual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.horario_label.configure(text=data_atual)
        self.after(1000, self.teste)
