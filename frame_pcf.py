import customtkinter
from functions_share import mostrar_usuarios, buscar_pessoa_registro, carregar_maquina, buscar_maquina_nome
from PIL import Image
from globals import nomeSelecionado
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import json

def resetarCoresBotoes(janela):
    for widget_pai in janela.winfo_children():
        for widget in widget_pai.winfo_children():
            if isinstance(widget_pai,customtkinter.CTkButton):
                widget_pai.configure(fg_color="transparent")

def mudarPessoa(pessoa, janela, frame_1):
    global nomeSelecionado
    nomeSelecionado = pessoa
    resetarCoresBotoes(frame_1)
    janela.configure(fg_color="blue")

class FramePcf(customtkinter.CTkFrame):
    def __init__(self, master, cod=None):
        self.maquinaLista = carregar_maquina()
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
        title_label.pack(pady=50)

        frame_total = customtkinter.CTkFrame(self,fg_color='transparent',width=501)
        frame_total.pack()

        user_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        user_frame.pack()
        userbox_frame = customtkinter.CTkFrame(user_frame, fg_color='transparent')
        userbox_frame.pack()
        default_frame = userbox_frame
        userbox_novo_frame = None
        usuario_carregados = mostrar_usuarios(cod)
        if usuario_carregados:
            for i in range(len(usuario_carregados)):
                if usuario_carregados[i]["Nome"] != None: 
                    if(i == 6):
                        userbox_novo_frame = customtkinter.CTkFrame(user_frame, fg_color='transparent',width=950)
                        userbox_novo_frame.pack()
                        default_frame = userbox_novo_frame
                    my_image = customtkinter.CTkImage(light_image=Image.open("config/imgs/users/"+usuario_carregados[i]["Imagem"]),dark_image=Image.open("config/imgs/users/"+usuario_carregados[i]["Imagem"]),size=(90, 90))
                    button_user = customtkinter.CTkButton(default_frame, image=my_image, compound="top", text=usuario_carregados[i]["Nome"].split(" ")[0],font=("Helvetica", 18, "bold"), fg_color="transparent", text_color='white')
                    button_user.configure(command=lambda arg1=usuario_carregados[i]["Registro"], arg2=button_user, arg3=userbox_frame: mudarPessoa(arg1, arg2, arg3))
                    button_user.pack(side='left', padx=8, pady=5)


        digitMaquina_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        digitMaquina_frame.pack(pady=5)
        maquinatitle_label = customtkinter.CTkLabel(digitMaquina_frame, justify="left", text="Maquina", font=("Helvetica", 20, "bold"), fg_color='transparent', width=950, anchor="w", text_color='white')
        maquinatitle_label.pack(pady=8)
        self.digt_maquina = customtkinter.CTkEntry(digitMaquina_frame, placeholder_text="Inserir Maquina", width=950, height=35, font=("Helvetica", 20))
        self.digt_maquina.pack()
        self.digt_maquina.bind("<KeyRelease>", self.sugestao_maquina)
        self.maquinasugestao_label = customtkinter.CTkFrame(digitMaquina_frame, fg_color='transparent', width=950,height=5)
        self.maquinasugestao_label.pack(side='left')

        digitComment_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        digitComment_frame.pack(pady=14)
        if cod == '0706':
            bloco_sintoma = customtkinter.CTkFrame(digitComment_frame, fg_color='transparent')
            bloco_sintoma.pack(side="left")
            sintomatitle_label = customtkinter.CTkLabel(bloco_sintoma, justify="left", text="Sintoma", font=("Helvetica", 20, "bold"), fg_color='transparent', width=315, anchor="w", text_color='white')
            sintomatitle_label.pack(pady=10, padx=2)
            self.digt_sintoma = customtkinter.CTkTextbox(bloco_sintoma, width=300, font=("Helvetica", 20))
            self.digt_sintoma.pack()

            bloco_causa = customtkinter.CTkFrame(digitComment_frame, fg_color='transparent')
            bloco_causa.pack(side="left")
            causatitle_label = customtkinter.CTkLabel(bloco_causa, justify="left", text="Causa", font=("Helvetica", 20, "bold"), fg_color='transparent', width=315, anchor="w", text_color='white')
            causatitle_label.pack(pady=10, padx=2)
            self.digt_causa = customtkinter.CTkTextbox(bloco_causa, width=300, font=("Helvetica", 20))
            self.digt_causa.pack()

            bloco_solucao = customtkinter.CTkFrame(digitComment_frame, fg_color='transparent')
            bloco_solucao.pack(side="left")
            solucaotitle_label = customtkinter.CTkLabel(bloco_solucao, justify="left", text="Solução", font=("Helvetica", 20, "bold"), fg_color='transparent', width=315, anchor="w", text_color='white')
            solucaotitle_label.pack(pady=10, padx=2)
            self.digt_solucao = customtkinter.CTkTextbox(bloco_solucao, width=300, font=("Helvetica", 20))
            self.digt_solucao.pack()       
        else:    
            comentariotitle_label = customtkinter.CTkLabel(digitComment_frame, justify="left", text="Comentario", font=("Helvetica", 20, "bold"), fg_color='transparent', width=950, anchor="w", text_color='white')
            comentariotitle_label.pack(pady=10)
            self.digt_comentario = customtkinter.CTkTextbox(digitComment_frame, width=950, font=("Helvetica", 20))
            self.digt_comentario.insert("0.0", "Verificando") 
            self.digt_comentario.focus_set()
            self.digt_comentario.pack()
            

        buttonSave_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        buttonSave_frame.pack(pady=20)
        button = customtkinter.CTkButton(buttonSave_frame, text="SALVAR",font=("Helvetica", 18, "bold"), fg_color='#6aa84f', text_color='white', width=850,height=40, command=lambda arg=cod:self.lancar_pcf(arg))
        button.pack(side='left', padx=8, pady=8)
        button = customtkinter.CTkButton(buttonSave_frame, text="LOTTO",font=("Helvetica", 18, "bold"), command=lambda arg="Modal": self.ir_para_lotto(arg), fg_color='#1155cc', text_color='white', width=80,height=40)
        button.pack(side='left', padx=8, pady=8)
        self.erros_label = customtkinter.CTkLabel(frame_total, text="", font=("Helvetica", 20), fg_color='transparent', text_color='white')
        self.erros_label.pack(pady=5)

    def ir_para_lotto(self, modal):
        global nomeSelecionado
        self.master.mostrar_pagina_lotto(modal, nomeSelecionado, self.digt_maquina.get())

    def pagina_inicial(self):
        self.master.mostrar_pagina_principal()


    def inserir_maquina(self, maquina):
        self.digt_maquina.delete(0, 'end')
        self.digt_maquina.insert(0, maquina)
        for widget in self.maquinasugestao_label.winfo_children():
                widget.destroy()

    def sugestao_maquina(self,event):
        entrada = self.digt_maquina.get().lower()
        for widget in self.maquinasugestao_label.winfo_children():
            widget.destroy()
        if len(entrada) > 3 :
            sugestoes = [d["maquina"] for d in self.maquinaLista if entrada in d["maquina"].lower()]
            for i in sugestoes:
                button = customtkinter.CTkButton(self.maquinasugestao_label, text=i,font=("Helvetica", 18), command=lambda arg=i: self.inserir_maquina(arg), fg_color='#1155cc', text_color='white', width=80,height=20)
                button.pack(padx=2, pady=3, side='left')
        
    
    def lancar_pcf(self, cod):
        maquina=self.digt_maquina.get().upper()
        maquinaInfos = buscar_maquina_nome(maquina, self.maquinaLista)
        if maquinaInfos is None:
            self.erros_label.configure(text="Maquina não encontrada")
            return 0
        if nomeSelecionado == "" or maquina == "" or maquina == "":
            self.erros_label.configure(text="Você deve preencher todos os campos")
            return 0
        usuario = buscar_pessoa_registro(nomeSelecionado)
        if usuario == None:
            self.erros_label.configure(text="registro informado não existe")
            return 0
        
        if cod == "0706":
            sintoma = self.digt_sintoma.get("0.0", "end")
            causa = self.digt_causa.get("0.0", "end")
            solucao = self.digt_solucao.get("0.0", "end")
            if solucao == "" or causa == "" or  sintoma == "":
                self.erros_label.configure(text="Você deve preencher todos os campos")
                return 0
            comentario = solucao.replace('\n', '')+" | "+causa.replace('\n', '')+" | "+sintoma.replace('\n', '')
            dados_salvar = {
                'registro': nomeSelecionado,
                'maquina': maquina,
                'data':datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                'sintoma': sintoma.replace('\n', ''),
                'causa': causa.replace('\n', ''),
                'solucao': solucao.replace('\n', '')
            }
            with open('G:\\SISTEMA MANUTENCAO\\bd\\pcFactory/liberacao.txt', 'a') as liberacao:
                json.dump(dados_salvar, liberacao)
                liberacao.write('\n')
        else:
            comentario = self.digt_comentario.get("0.0", "end")
            if comentario =="" :
                self.erros_label.configure(text="Você deve preencher todos os campos")
                return 0
        self.master.mostrar_pagina_principal()

        #servico = Service("drivers/chromedriver.exe")
        #navegador = webdriver.Chrome(service=servico)
        #navegador.get("http://10.36.216.25:9097/") #entrar no site
        #WebDriverWait(navegador, 120).until(
        #    EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')) #escrever no login
        #).send_keys(usuario['Registro'])
        #WebDriverWait(navegador, 120).until(
        #    EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')) #escever senha
        #).send_keys(usuario['Senha'])
        #WebDriverWait(navegador, 120).until(
        #    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-authentication/div/div/div/div[2]/form/app-button[1]/button'))
        #).click() #click em logar
        #WebDriverWait(navegador, 120).until(
        #    EC.element_to_be_clickable((By.XPATH, ''))
        #).click() #click em mapa
        #WebDriverWait(navegador, 120).until(
        #    EC.element_to_be_clickable((By.XPATH, ''))
        #).click() #click na planta
        #WebDriverWait(navegador, 120).until(
        #    EC.element_to_be_clickable((By.XPATH, ''))
        #).click() #click maquina
        #WebDriverWait(navegador, 120).until(
        #    EC.element_to_be_clickable((By.XPATH, ''))
        #).click() #click parada
        #WebDriverWait(navegador, 120).until(
        #    EC.element_to_be_clickable((By.XPATH, ''))
        #).click() #click em tipo
        #WebDriverWait(navegador, 120).until(
        #    EC.element_to_be_clickable((By.XPATH, ''))
        #).click() #click em status
        #WebDriverWait(navegador, 120).until(
        #    EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')) #escrever no login
        #).send_keys(comentario) #digitar comentarto
        #WebDriverWait(navegador, 120).until(
        #    EC.element_to_be_clickable((By.XPATH, ''))
        #).click() #click em salvar