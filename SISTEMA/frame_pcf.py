import customtkinter
from functions_share import mostrar_usuarios
from PIL import Image
from globals import nomeSelecionado

def resetarCoresBotoes(janela):
    for widget in janela.winfo_children():
        if isinstance(widget, customtkinter.CTkButton):
            widget.configure(fg_color="transparent")

def mudarPessoa(pessoa, janela, frame):
    global nomeSelecionado
    nomeSelecionado = pessoa
    resetarCoresBotoes(frame)
    janela.configure(fg_color="blue")

class FramePcf(customtkinter.CTkFrame):
    def __init__(self, master, cod=None):
        list_pcf={
            None: "",
            "0405": "Elétrico",
            "0406": "Hidráulico",
            "0407": "Mecânico",
            "0408": "Pneumático",
            "0403": "Análise",
            "0706": "Liberar",
            "0502": "Pre-Elétrico",
            "0504": "Pre-Hidráulico",
            "0505": "Pre-Mecânico",
            "0506": "Pre-Pneumático",
            "0404": "BCR",
            "0418": "Ajus.Parâmetro",
        }
        customtkinter.CTkFrame.__init__(self, master, fg_color='transparent')
        title_label = customtkinter.CTkLabel(self, text=str(list_pcf[cod]).upper(), font=("Helvetica", 70, "bold"), fg_color='transparent', text_color='white')
        title_label.pack(pady=80)

        frame_total = customtkinter.CTkFrame(self,fg_color='transparent',width=501)
        frame_total.pack()

        user_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        user_frame.pack()
        usertitle_label = customtkinter.CTkLabel(user_frame, text="Usuario", font=("Helvetica", 20, "bold"), fg_color='transparent',width=950, anchor="w", text_color='white')
        usertitle_label.pack()
        userbox_frame = customtkinter.CTkFrame(user_frame, fg_color='transparent',width=950)
        userbox_frame.pack(side='left')
        usuario_carregados = mostrar_usuarios(cod)
        if usuario_carregados:
            for i in range(len(usuario_carregados)):
                if usuario_carregados[i]["Nome"] != None: 
                    my_image = customtkinter.CTkImage(light_image=Image.open("config/imgs/users/"+usuario_carregados[i]["Imagem"]),dark_image=Image.open("config/imgs/users/"+usuario_carregados[i]["Imagem"]),size=(90, 110))
                    button_user = customtkinter.CTkButton(userbox_frame, image=my_image, compound="top", text=usuario_carregados[i]["Nome"],font=("Helvetica", 18, "bold"), fg_color="transparent", text_color='white')
                    button_user.configure(command=lambda arg1=usuario_carregados[i]["Nome"], arg2=button_user, arg3=userbox_frame: mudarPessoa(arg1, arg2, arg3))
                    button_user.pack(side='left', padx=8, pady=8)

        digitMaquina_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        digitMaquina_frame.pack(pady=20)
        self.digt_maquina = customtkinter.CTkEntry(digitMaquina_frame, placeholder_text="Inserir Maquina", width=950, height=35, font=("Helvetica", 20))
        self.digt_maquina.pack()

        digitComment_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        digitComment_frame.pack(pady=20)
        maquinatitle_label = customtkinter.CTkLabel(digitComment_frame, justify="left", text="Comentario", font=("Helvetica", 20, "bold"), fg_color='transparent', width=950, anchor="w", text_color='white')
        maquinatitle_label.pack(pady=10)
        digt_comentario = customtkinter.CTkTextbox(digitComment_frame, width=950, font=("Helvetica", 20))
        digt_comentario.pack()

        buttonSave_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        buttonSave_frame.pack(pady=20)
        button = customtkinter.CTkButton(buttonSave_frame, text="SALVAR",font=("Helvetica", 18, "bold"), fg_color='#6aa84f', text_color='white', width=850,height=40)
        button.pack(side='left', padx=8, pady=8)
        button = customtkinter.CTkButton(buttonSave_frame, text="LOTTO",font=("Helvetica", 18, "bold"), command=lambda arg="Modal": self.ir_para_lotto(arg), fg_color='#1155cc', text_color='white', width=80,height=40)
        button.pack(side='left', padx=8, pady=8)

    def ir_para_lotto(self, modal):
        global nomeSelecionado
        self.master.mostrar_pagina_lotto(modal, nomeSelecionado, self.digt_maquina.get())

    def pagina_inicial(self):
        self.master.mostrar_pagina_principal()