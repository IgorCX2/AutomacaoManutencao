import customtkinter
from app_functions import *

from frame_principal import FramePrincipal
from frame_descanso import FrameDescanso
from frame_lotto import FrameLotto
from frame_pcf import FramePcf

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Aplicativo(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)
        self.pagina_ativa = None
        button_inicio = customtkinter.CTkButton(self, text="Página Inicial", font=("Helvetica", 12), fg_color='transparent', text_color='white', command=self.mostrar_pagina_principal)
        button_inicio.place(x=0, y=0) 
        self.tempo_inativo = 0
        self.bind("<Motion>", lambda event: reiniciar_temporizador(self, event))

        self.frame_principal = FramePrincipal(self)
        self.frame_descanso = FrameDescanso(self)
        self.frame_lotto = FrameLotto(self)
        self.frame_pcf = FramePcf(self)

        
        #Adc caminho das novas paginas
        self.paginas = {
            "principal": self.mostrar_pagina_principal,
            "descanso": self.mostrar_pagina_descanso,
            "lotto": self.mostrar_pagina_lotto,
            "pcf": self.mostrar_pagina_pcf,
        }
        self.mostrar_pagina_principal()

    def verificar_inatividade(self):
        self.after(1000, lambda: verificar_inatividade(self))

    #Adc caminho das novas paginas
    def mostrar_pagina_principal(self):
        self.pagina_ativa = "principal"
        mostrar_pagina_principal(self)

    def mostrar_pagina_pcf(self, cod):
        self.pagina_ativa = "pcf"
        mostrar_pagina_pcf(self, cod)

    def mostrar_pagina_descanso(self):
        self.pagina_ativa = None
        mostrar_pagina_descanso(self)

    def mostrar_pagina_lotto(self, modal,usuario,maquina):
        self.pagina_ativa = "lotto"
        mostrar_pagina_lotto(self, modal,usuario,maquina)

if __name__ == "__main__":
    app = Aplicativo()
    app.verificar_inatividade()
    app.mainloop()