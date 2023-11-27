import customtkinter

class FrameDescanso(customtkinter.CTkFrame):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(self, master)
        self.master = master
        self.label = customtkinter.CTkLabel(self, text="Pensando em algo incrivel =)")
        self.label.pack(pady=20)
        #self.after(5000, self.master.mostrar_pagina_principal)  para voltar depois de 5s com ou sem inatividade