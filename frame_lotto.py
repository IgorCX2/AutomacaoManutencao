import customtkinter
from datetime import datetime
import json
from functions_share import pesquisar_chave_arquivo, buscar_chave_no_temporario, buscar_pessoa_registro, chaves_usando, carregar_maquina, buscar_maquina_nome

class FrameLotto(customtkinter.CTkFrame):
    def __init__(self, master,modal=None, usuario=None, maquina=None, dataAtual=None):
        self.maquinaLista = carregar_maquina()
        customtkinter.CTkFrame.__init__(self, master, fg_color='transparent')
        self.master = master
        self.digit_maquina = False
        self.digit_registro = False
        self.label = customtkinter.CTkLabel(self, text="LOTTO", font=("Helvetica", 60, "bold"), fg_color='transparent', text_color='white')
        self.label.pack(pady=50)
        frame_lotto = customtkinter.CTkFrame(self,fg_color='transparent',width=501)
        frame_lotto.pack(pady=25)
        lotto_form_frame = customtkinter.CTkFrame(frame_lotto, fg_color='transparent')
        lotto_form_frame.pack(side='top')

        lotto_inicial_frame = customtkinter.CTkFrame(lotto_form_frame, fg_color='transparent',width=950)
        lotto_inicial_frame.pack()
        lotto_frame = customtkinter.CTkFrame(lotto_inicial_frame, fg_color='transparent',width=950)
        lotto_frame.pack(side='left',padx=8)
        chave_title_label = customtkinter.CTkLabel(lotto_frame, text="Chave", font=("Helvetica", 20, "bold"), fg_color='transparent',width=450, anchor="w", text_color='white')
        chave_title_label.pack(pady=10)
        self.digt_chave = customtkinter.CTkEntry(lotto_frame, width=450, height=35, font=("Helvetica", 20))
        self.digt_chave.pack()
        self.digt_chave.bind("<KeyRelease>", lambda event: self.pesquisar_chave(event, usuario, maquina))
        lotto_frame = customtkinter.CTkFrame(lotto_inicial_frame, fg_color='transparent',width=950)
        lotto_frame.pack(side='left',padx=10)

        maquina_title_label = customtkinter.CTkLabel(lotto_frame, text="Maquina", font=("Helvetica", 20, "bold"), fg_color='transparent',width=450, anchor="w", text_color='white')
        maquina_title_label.pack(pady=10)
        self.digt_maquina = customtkinter.CTkEntry(lotto_frame,width=450,height=35, font=("Helvetica", 20))
        if maquina:
            self.digt_maquina.insert(0, maquina)
        self.digt_maquina.pack()
        self.digt_maquina.bind("<KeyRelease>", self.sugestao_maquina)
        self.maquinasugestao_label = customtkinter.CTkFrame(lotto_form_frame, fg_color='transparent', width=450,height=5)
        self.maquinasugestao_label.pack(side='top')
        lotto_inicial_frame = customtkinter.CTkFrame(lotto_form_frame, fg_color='transparent',width=950)
        lotto_inicial_frame.pack(pady=45)
        lotto_frame = customtkinter.CTkFrame(lotto_inicial_frame, fg_color='transparent',width=950)
        lotto_frame.pack(side='left',padx=8)
        registro_title_label = customtkinter.CTkLabel(lotto_frame, text="Registro", font=("Helvetica", 20, "bold"), fg_color='transparent',width=600, anchor="w", text_color='white')
        registro_title_label.pack(pady=10)
        self.digt_registro = customtkinter.CTkEntry(lotto_frame,width=600,height=35, font=("Helvetica", 20))
        if usuario:
            self.digt_registro.insert(0, usuario)
        self.digt_registro.pack()
        self.digt_registro.bind("<KeyRelease>", self.salvar_registro_digit)
        lotto_frame = customtkinter.CTkFrame(lotto_inicial_frame, fg_color='transparent',width=950)
        lotto_frame.pack(side='left',padx=10)
        data_title_label = customtkinter.CTkLabel(lotto_frame, text="Data", font=("Helvetica", 20, "bold"), fg_color='transparent',width=300, anchor="w", text_color='white')
        data_title_label.pack(pady=10)
        self.digt_data = customtkinter.CTkEntry(lotto_frame,width=300,height=35, font=("Helvetica", 20))
        self.digt_data.insert(0, str(dataAtual))
        self.digt_data.pack()
        lotto_inicial_frame = customtkinter.CTkFrame(lotto_form_frame, fg_color='transparent',width=950)
        lotto_inicial_frame.pack()	
        button = customtkinter.CTkButton(lotto_inicial_frame, text="SALVAR",font=("Helvetica", 18, "bold"), fg_color='#6aa84f', text_color='white', width=300, height=40, command=lambda arg=modal: self.executar_operacao(arg))
        button.pack()
        self.erros_label = customtkinter.CTkLabel(lotto_inicial_frame, text="", font=("Helvetica", 20), fg_color='transparent', text_color='white')
        self.erros_label.pack(pady=15)
        self.lotto_inicial_frame = customtkinter.CTkFrame(lotto_form_frame, fg_color='transparent',width=950)
        self.lotto_inicial_frame.pack()	
        self.config_lista = self.atualizar_lista_cadeados(self.lotto_inicial_frame,chaves_usando())
        
    def atualizar_lista_cadeados(event, janela, chaveInfos):
        for widget in janela.winfo_children():
            widget.destroy()
        lottoInfo_frame = customtkinter.CTkFrame(janela,width=950,fg_color='transparent')
        lottoInfo_frame.pack(side='left',pady=15)
        infos_label = customtkinter.CTkLabel(lottoInfo_frame, text="INFORMAÇÕES",width=950, font=("Helvetica", 25, "bold"), fg_color='transparent', text_color='white')
        infos_label.pack(pady=25)
        lotto_inicial_frame = customtkinter.CTkFrame(lottoInfo_frame, fg_color='transparent',width=950)
        lotto_inicial_frame.pack()	

        infos_lateral_frame = customtkinter.CTkScrollableFrame(lotto_inicial_frame,width=450)
        infos_lateral_frame.pack(side='left',padx=10)
        titulo_lateral_label = customtkinter.CTkLabel(infos_lateral_frame, text="DISPONÍVEL",width=445, font=("Helvetica", 20, "bold"), fg_color='transparent', text_color='white')
        titulo_lateral_label.pack(pady=10)
        for chaveInfo in chaveInfos["chaves_livre"]:
            cad_livre_label = customtkinter.CTkLabel(infos_lateral_frame, text=chaveInfo,font=("Helvetica", 18), width=370,anchor="w", fg_color='transparent', text_color='white')
            cad_livre_label.pack(pady=2)

        infos_lateral_frame = customtkinter.CTkScrollableFrame(lotto_inicial_frame,width=445)
        infos_lateral_frame.pack(side='top',padx=10)
        titulo_lateral_label = customtkinter.CTkLabel(infos_lateral_frame, text="UTILIZANDO",width=445, font=("Helvetica", 20, "bold"), fg_color='transparent', text_color='white')
        titulo_lateral_label.pack(pady=10)
        for chaveInfo in chaveInfos["chaves_usando"]:
            cad_usando_label = customtkinter.CTkLabel(infos_lateral_frame, text=chaveInfo,font=("Helvetica", 18), width=370,anchor="w", fg_color='transparent', text_color='white')
            cad_usando_label.pack(pady=2)

        #lotto_inicial_frame = customtkinter.CTkFrame(lottoInfo_frame, fg_color='#ff8c00',width=908, height=50)
        #lotto_inicial_frame.pack(pady=20, padx=10)
        #titulo_lateral_label = customtkinter.CTkLabel(lotto_inicial_frame, text="UTILIZANDO", font=("Helvetica", 20), fg_color='transparent', text_color='white')
        #titulo_lateral_label.pack(pady=10,  padx=10,side="left")
        
    def salvar_registro_digit(self, event):
         self.digit_registro = True

    def inserir_maquina(self, maquina):
        self.digt_maquina.delete(0, 'end')
        self.digt_maquina.insert(0, maquina)
        for widget in self.maquinasugestao_label.winfo_children():
                widget.destroy()

    def sugestao_maquina(self,event):
        entrada = self.digt_maquina.get().lower()
        self.digit_maquina = entrada
        for widget in self.maquinasugestao_label.winfo_children():
            widget.destroy()
        if len(entrada) > 3 :
            sugestoes = [d["maquina"] for d in self.maquinaLista if entrada in d["maquina"].lower()]
            for i in sugestoes:
                button = customtkinter.CTkButton(self.maquinasugestao_label, text=i,font=("Helvetica", 18), command=lambda arg=i: self.inserir_maquina(arg), fg_color='#1155cc', text_color='white', width=80,height=20)
                button.pack(padx=2, pady=3, side='left')

    def pesquisar_chave(self, event,usuario, maquina):
        chave_procurada = self.digt_chave.get()
        lottoChave = pesquisar_chave_arquivo(chave_procurada)
        if lottoChave:
            lottoHistorico = buscar_chave_no_temporario(chave_procurada)
            if lottoHistorico:
                self.label.configure(text="LIBERAR LOTTO")
                self.digt_maquina.delete(0, 'end')
                self.digt_maquina.insert(0, lottoHistorico['maquina'])
                if usuario is None and self.digit_registro == False:
                    self.digt_registro.delete(0, 'end')
                    self.digt_registro.insert(0, lottoHistorico['registro_bloquear'])
                    return 0
            else:
                self.label.configure(text="REALIZAR LOTTO")
                chave_realizar_lotto = pesquisar_chave_arquivo(chave_procurada)
                if maquina is not None and maquina != "":
                    self.digt_maquina.delete(0, 'end')
                    self.digt_maquina.insert(0, maquina)
                else:
                    if self.digit_maquina:
                        print(self.digit_maquina)
                        self.digt_maquina.delete(0, 'end')
                        self.digt_maquina.insert(0, self.digit_maquina)
                #self.digt_maquina.delete(0, 'end') tinha return no if/
                #self.digt_maquina.insert(0, "")
                if usuario is None and self.digit_registro == False:
                    self.digt_registro.delete(0, 'end')
                    self.digt_registro.insert(0, chave_realizar_lotto['proprietario'])
        else:
            self.label.configure(text="S/ CHAVE LOTTO")

    def executar_operacao(self, modal):
        Erro = True
        chave = self.digt_chave.get()
        registro = self.digt_registro.get()
        maquina = self.digt_maquina.get().upper()
        data = self.digt_data.get()
        maquinaInfos = buscar_maquina_nome(maquina, self.maquinaLista)
        if maquinaInfos is None:
            self.erros_label.configure(text="Maquina não encontrada")
            return 0
        if chave == "" or registro == "" or maquina == "" or data == "":
            self.erros_label.configure(text="Você deve preencher todos os campos")
            return 0
        chave_buscado = pesquisar_chave_arquivo(chave)
        if chave_buscado == None:
            self.erros_label.configure(text="chave nao cadastrada")
            return 0
        registro_buscado = buscar_pessoa_registro(registro)
        if registro_buscado == None:
            self.erros_label.configure(text="registro informado não existe")
            return 0
        if buscar_chave_no_temporario(chave):
            with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\temporario.txt', 'r') as arquivo_temporario:
                linhas = arquivo_temporario.readlines()

            with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\temporario.txt', 'w') as arquivo_temporario:
                for linha in linhas:
                    dados_registro = json.loads(linha)
                    if dados_registro['chave'] == chave:
                        linha_excluida = json.loads(linha)
                        buscar_registro_chave_realizada = buscar_pessoa_registro(linha_excluida["registro_bloquear"])
                        if registro_buscado["Cargo"] != buscar_registro_chave_realizada["Cargo"] or linha_excluida["maquina"] != maquina:
                            Erro = False
                            if linha_excluida["maquina"] != maquina:
                                self.erros_label.configure(text="O lotto deste cadeado está na máquina "+linha_excluida["maquina"]+"!")
                            else:
                                self.erros_label.configure(text="Você não pode desbloquear um lotto "+buscar_registro_chave_realizada["Cargo"]+" sendo um "+registro_buscado["Cargo"])
                            json.dump(dados_registro, arquivo_temporario)
                            arquivo_temporario.write('\n')
                    else:
                        json.dump(dados_registro, arquivo_temporario)
                        arquivo_temporario.write('\n')

            with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\aprovacao.txt', 'a') as arquivo_aprovar:
                dados_registro = {
                    'chave': linha_excluida['chave'],
                    'maquina': linha_excluida['maquina'],
                    'registro_bloquear': linha_excluida['registro_bloquear'],
                    "registro_desbloquear" : registro,
                    'data_bloquear': linha_excluida['data_bloquear'],
                    'data_desbloquear': data,
                    'verificador_bloqueio': linha_excluida['verificador_bloqueio'],
                    'verificador_data_bloqueio': linha_excluida['verificador_data_bloqueio'],
                    'verificador_desbloqueio': '',
                    'verificador_data_desbloqueio': ''
                }
                json.dump(dados_registro, arquivo_aprovar)
                arquivo_aprovar.write('\n')
        else:
            if registro_buscado["Cargo"] != chave_buscado["tipo"] and chave_buscado["tipo"] != "Comunitario" :
                self.erros_label.configure(text="Você não pode bloquear em um cadeado "+chave_buscado["tipo"]+" sendo um "+registro_buscado["Cargo"])
                return 0
            dados_registro = {
                'chave': chave,
                'maquina': maquina,
                'registro_bloquear': registro,
                'data_bloquear': data,
                'verificador_bloqueio': '',
                'verificador_data_bloqueio': ''
            }

            with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\temporario.txt', 'a') as arquivo_temporario:
                json.dump(dados_registro, arquivo_temporario)
                arquivo_temporario.write('\n')
        if Erro:
            self.config_lista = self.atualizar_lista_cadeados(self.lotto_inicial_frame,chaves_usando())
            self.digt_chave.delete(0, 'end')
            self.digt_registro.delete(0, 'end')
            self.digt_maquina.delete(0, 'end')
            self.digit_maquina = False
            self.digit_registro = False
            self.label.configure(text="CHAVE LOTTO")
            self.erros_label.configure(text="")
            if modal == "Modal":
                self.master.destroy()
            else:
                self.master.mostrar_pagina_principal()