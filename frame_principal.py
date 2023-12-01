import customtkinter

class FramePrincipal(customtkinter.CTkFrame):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(self, master, fg_color='transparent')
        title_label = customtkinter.CTkLabel(self, text="SISTEMA MANUTENÇÃO", font=("Helvetica", 70, "bold"), fg_color='transparent', text_color='white')
        title_label.pack(pady=90)
        buttons_cod=[["0405","0406","0407","0408","0403","0706"],["0502","0504","0505","0506","0404","0418"]]
        buttons_txt=[["Elétrico","Hidráulico","Mecânico","Pneumático","Análise","Liberar"],["Pre-Elétrico","Pre-Hidráulico","Pre-Mecânico","Pre-Pneumático","BCR","Ajus.Parâmetro"]]
        main_frame = customtkinter.CTkFrame(self, fg_color='transparent')
        main_frame.pack(pady=20)
        for i in range(2):
            button_frame = customtkinter.CTkFrame(main_frame, fg_color='transparent')
            button_frame.pack()
            for c in range(len(buttons_cod[i])):
                button = customtkinter.CTkButton(button_frame, text=buttons_txt[i][c], command=lambda arg=buttons_cod[i][c]: self.ir_para_pcf(arg), width=153, height=120, font=("Helvetica", 18, "bold"), fg_color='white', text_color='dark blue')
                button.pack(side='left', padx=8, pady=8)

        button_frame = customtkinter.CTkFrame(main_frame, fg_color='transparent')
        button_frame.pack()
        button = customtkinter.CTkButton(button_frame, text="SISTEMA LOTTO", font=("Helvetica", 18, "bold"),  command=lambda arg="naoModal": self.ir_para_lotto(arg), width=652, height=120, fg_color='white', text_color='dark blue')
        button.pack(side='left', padx=8, pady=8)
        button = customtkinter.CTkButton(button_frame, text="BCR", font=("Helvetica", 18, "bold"), width=153, height=120, fg_color='white', text_color='dark blue')
        button.pack(side='left', padx=8, pady=8)
        button = customtkinter.CTkButton(button_frame, text="LIMPEZA", font=("Helvetica", 18, "bold"), width=153, height=120, fg_color='white', text_color='dark blue')
        button.pack(side='left', padx=8, pady=8)

    def ir_para_lotto(self, modal):
        self.master.mostrar_pagina_lotto(modal, "", "")

    def ir_para_pcf(self, cod):
        self.master.mostrar_pagina_pcf(cod)