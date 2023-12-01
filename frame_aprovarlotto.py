import customtkinter
import json
import tkinter as tk
from functions_share import chaves_para_verificar
from datetime import datetime

class FrameAprovaLotto(customtkinter.CTkFrame):
    def __init__(self, master, user=None):
        customtkinter.CTkFrame.__init__(self, master, fg_color='transparent')
        title_label = customtkinter.CTkLabel(self, text="APROVAR LOTTO", font=("Helvetica", 70, "bold"), fg_color='transparent', text_color='white')
        title_label.pack(pady=90)
        self.lotto_inicial_frame = customtkinter.CTkScrollableFrame(self, fg_color='transparent',width=1000, height=700)
        self.lotto_inicial_frame.pack()	
        self.config_lista = self.atualizar_aprovar(self.lotto_inicial_frame, user)
    


    def atualizar_aprovar(self, janela, usuario):
        for widget in janela.winfo_children():
            widget.destroy()
        buscar_chaves = chaves_para_verificar()
        for i in range(len(buscar_chaves['ChaveAberta'])):
            chaveAtual = json.loads(buscar_chaves['ChaveAberta'][i])
            if chaveAtual["verificador_bloqueio"] == "":
                lottoBloco_frame = customtkinter.CTkFrame(janela,width=1000)
                lottoBloco_frame.pack(pady=15)
                infos_label = customtkinter.CTkLabel(lottoBloco_frame, text=chaveAtual["chave"],width=950, font=("Helvetica", 25, "bold"), fg_color='transparent', text_color='white')
                infos_label.pack(pady=25)
                button = customtkinter.CTkButton(lottoBloco_frame, text="VERIFICAR BLOQUEIO",font=("Helvetica", 18, "bold"), fg_color='#6aa84f', text_color='white', height=40, command=lambda arg=usuario, arg1=i, arg2=janela: self.verificar_bloqueio(arg,arg1,arg2))
                button.pack(side='left', padx=8, pady=8)

        for i in range(len(buscar_chaves['ChaveFechada'])):
            chaveAtual = json.loads(buscar_chaves['ChaveFechada'][i])
            if chaveAtual["verificador_bloqueio"] == "" or chaveAtual["verificador_desbloqueio"] == "":
                lottoBloco_frame = customtkinter.CTkFrame(janela,width=950)
                lottoBloco_frame.pack(pady=15)
                infos_label = customtkinter.CTkLabel(lottoBloco_frame, text=chaveAtual["chave"],width=950, font=("Helvetica", 25, "bold"), fg_color='transparent', text_color='white')
                infos_label.pack(pady=25)
                if chaveAtual["verificador_bloqueio"] == "":
                    button = customtkinter.CTkButton(lottoBloco_frame, text="VERIFICAR BLOQUEIO",font=("Helvetica", 18, "bold"), fg_color='#6aa84f', text_color='white', height=40, command=lambda arg=usuario, arg1=i, arg2=janela, arg3="bloqueio", arg4=chaveAtual: self.verificar_arquivo_aprovacao(arg,arg1,arg2,arg3,arg4))
                    button.pack(side='left', padx=8, pady=8)
                if chaveAtual["verificador_desbloqueio"] == "":
                    button = customtkinter.CTkButton(lottoBloco_frame, text="VERIFICAR DESBLOQUEIO",font=("Helvetica", 18, "bold"), fg_color='#6aa84f', text_color='white', height=40, command=lambda arg=usuario, arg1=i, arg2=janela, arg3="desbloqueio", arg4=chaveAtual: self.verificar_arquivo_aprovacao(arg,arg1,arg2,arg3,arg4))
                    button.pack(side='left', padx=8, pady=8)

    def verificar_bloqueio(self, usuario, linha, janela):
        with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\temporario.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            minhaLinha = json.loads(linhas[linha])
        dados_atualizar = {
            'chave': minhaLinha["chave"],
            'maquina': minhaLinha["maquina"],
            'registro_bloquear': minhaLinha["registro_bloquear"],
            'data_bloquear': minhaLinha["data_bloquear"],
            'verificador_bloqueio': usuario["Registro"],
            'verificador_data_bloqueio': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        linhas[linha] = f'{json.dumps(dados_atualizar)}\n'
        with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\temporario.txt', 'w') as arquivo:
            arquivo.writelines(linhas)
        self.config_lista = self.atualizar_aprovar(janela, usuario)

    def verificar_arquivo_aprovacao(self, usuario, linha, janela, acao, chave):
        if chave["verificador_bloqueio"] == "" and chave["verificador_desbloqueio"] == "":
            with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\aprovacao.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                minhaLinha = json.loads(linhas[linha])
            if acao == "desbloqueio":
                dados_atualizar = {
                    'chave': minhaLinha["chave"],
                    'maquina': minhaLinha["maquina"],
                    'registro_bloquear': minhaLinha["registro_bloquear"],
                    'registro_desbloquear':  minhaLinha["registro_desbloquear"],
                    'data_bloquear': minhaLinha["data_bloquear"],
                    'data_desbloquear': minhaLinha["data_desbloquear"],
                    'verificador_bloqueio': "",
                    'verificador_data_bloqueio': "",
                    "verificador_desbloqueio": usuario["Registro"],
                    "verificador_data_desbloqueio":datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                }
            else:
                dados_atualizar = {
                    'chave': minhaLinha["chave"],
                    'maquina': minhaLinha["maquina"],
                    'registro_bloquear': minhaLinha["registro_bloquear"],
                    'registro_desbloquear':  minhaLinha["registro_desbloquear"],
                    'data_bloquear': minhaLinha["data_bloquear"],
                    'data_desbloquear': minhaLinha["data_desbloquear"],
                    'verificador_bloqueio': usuario["Registro"],
                    'verificador_data_bloqueio': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "verificador_desbloqueio": "",
                    "verificador_data_desbloqueio":""
                }
            linhas[linha] = f'{json.dumps(dados_atualizar)}\n'
            with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\aprovacao.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            self.config_lista = self.atualizar_aprovar(janela, usuario)
        else:
            with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\aprovacao.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                
            with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\aprovacao.txt', 'w') as arquivo:
                for i, l in enumerate(linhas):
                    if i != linha:
                        arquivo.write(l)
                    else:
                        minhaLinha = json.loads(l)
                        if acao == "desbloqueio":
                            dados_atualizar = {
                                'chave': minhaLinha["chave"],
                                'maquina': minhaLinha["maquina"],
                                'registro_bloquear': minhaLinha["registro_bloquear"],
                                'registro_desbloquear':  minhaLinha["registro_desbloquear"],
                                'data_bloquear': minhaLinha["data_bloquear"],
                                'data_desbloquear': minhaLinha["data_desbloquear"],
                                'verificador_bloqueio': minhaLinha["verificador_bloqueio"],
                                'verificador_data_bloqueio': minhaLinha["verificador_data_bloqueio"],
                                "verificador_desbloqueio": usuario["Registro"],
                                "verificador_data_desbloqueio":datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                            }
                        else:
                            dados_atualizar = {
                                'chave': minhaLinha["chave"],
                                'maquina': minhaLinha["maquina"],
                                'registro_bloquear': minhaLinha["registro_bloquear"],
                                'registro_desbloquear':  minhaLinha["registro_desbloquear"],
                                'data_bloquear': minhaLinha["data_bloquear"],
                                'data_desbloquear': minhaLinha["data_desbloquear"],
                                'verificador_bloqueio': usuario["Registro"],
                                'verificador_data_bloqueio': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                                "verificador_desbloqueio": minhaLinha["verificador_desbloqueio"],
                                "verificador_data_desbloqueio":minhaLinha["verificador_data_desbloqueio"]
                            }
                        with open('G:\\SISTEMA MANUTENCAO\\bd\\loto\\historico.txt', 'a') as historico:
                            json.dump(dados_atualizar, historico)
                            historico.write('\n')

        self.config_lista = self.atualizar_aprovar(janela, usuario)