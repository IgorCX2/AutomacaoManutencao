import customtkinter
from functions_share import buscar_pessoa_registro

class FrameAdmLogin(customtkinter.CTkFrame):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(self, master, fg_color='transparent')
        title_label = customtkinter.CTkLabel(self, text="LOGIN", font=("Helvetica", 70, "bold"), fg_color='transparent', text_color='white')
        title_label.pack(pady=60)
        frame_total = customtkinter.CTkFrame(self,fg_color='transparent',width=501)
        frame_total.pack()
        registro_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        registro_frame.pack(pady=20)
        registro_label = customtkinter.CTkLabel(registro_frame, justify="left", text="Registro", font=("Helvetica", 20, "bold"), fg_color='transparent', width=500, anchor="w", text_color='white')
        registro_label.pack(pady=10)
        self.registro = customtkinter.CTkEntry(registro_frame, placeholder_text="Inserir Registro", width=500, height=35, font=("Helvetica", 20))
        self.registro.pack()
        senha_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        senha_frame.pack(pady=20)
        senha_label = customtkinter.CTkLabel(senha_frame, justify="left", text="Senha", font=("Helvetica", 20, "bold"), fg_color='transparent', width=500, anchor="w", text_color='white')
        senha_label.pack(pady=10)
        self.senha = customtkinter.CTkEntry(senha_frame, placeholder_text="Inserir Senha", width=500, height=35, font=("Helvetica", 20))
        self.senha.pack()
        button = customtkinter.CTkButton(frame_total, text="ENTRAR",font=("Helvetica", 18, "bold"), fg_color='#6aa84f', text_color='white', width=500, height=40, command=self.entrar_sistema)
        button.pack(side='left', padx=8, pady=8)
        self.erros_label = customtkinter.CTkLabel(frame_total, text="", font=("Helvetica", 20), fg_color='transparent', text_color='white')
        self.erros_label.pack(pady=15)
    
    def entrar_sistema(self):
        senha = self.senha.get()
        registro = self.registro.get()
        if senha == "" or registro == "":
            self.erros_label.configure(text="Você deve preencher todos os campos")
            return 0
        trazerUsuario = buscar_pessoa_registro(registro)
        if trazerUsuario == None:
            self.erros_label.configure(text="registro informado não existe")
            return 0
        if trazerUsuario["Cargo"] != "Adm":
            self.erros_label.configure(text="voce nao tem permicao de acesso!")
            return 0
        if trazerUsuario["Senha"] == senha:
            self.erros_label.configure(text="")
            self.senha.delete(0, 'end')
            self.registro.delete(0, 'end')
            self.master.mostrar_pagina_adm(trazerUsuario)
        else:
            self.erros_label.configure(text="senha incorreta")
            return 0
        