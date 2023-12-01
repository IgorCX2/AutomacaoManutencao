import time
import customtkinter
from datetime import datetime
from frame_pcf import FramePcf
from frame_lotto import FrameLotto
from frame_aprovarlotto import FrameAprovaLotto
from frame_adm import FrameAdm

def reiniciar_temporizador(app, event):
    app.tempo_inativo = time.time()

def verificar_inatividade(app):
    app.after(1000, lambda: verificar_inatividade(app))

    if time.time() - app.tempo_inativo > 120:
        app.mostrar_pagina_descanso()
        app.pagina_ativa = None
        return 0
    elif app.pagina_ativa != None:
        return 0
    else:
        app.mostrar_pagina_principal()
        return 0

#Adc caminho das novas paginas

def mostrar_aprovarlotto(app, user):
    app.frame_adm.pack_forget()
    app.frame_lotto.pack_forget()
    app.frame_descanso.pack_forget()
    app.frame_principal.pack_forget()
    app.frame_pcf.pack_forget()
    app.frame_login.pack_forget()
    app.frame_aprovarlotto = FrameAprovaLotto(app, user) 
    app.frame_aprovarlotto.pack()

def mostrar_pagina_login(app):
    app.frame_adm.pack_forget()
    app.frame_lotto.pack_forget()
    app.frame_descanso.pack_forget()
    app.frame_principal.pack_forget()
    app.frame_pcf.pack_forget()
    app.frame_aprovarlotto.pack_forget()
    app.frame_login.pack()

def mostrar_pagina_adm(app,user):
    app.frame_lotto.pack_forget()
    app.frame_descanso.pack_forget()
    app.frame_principal.pack_forget()
    app.frame_pcf.pack_forget()
    app.frame_login.pack_forget()
    app.frame_aprovarlotto.pack_forget()
    app.frame_adm = FrameAdm(app, user)
    app.frame_adm.pack()

def mostrar_pagina_pcf(app, cod):
    app.title("Reporte"+" "+cod)
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight())) 
    app.frame_adm.pack_forget()
    app.frame_login.pack_forget()
    app.frame_lotto.pack_forget()
    app.frame_descanso.pack_forget()
    app.frame_principal.pack_forget()
    app.frame_aprovarlotto.pack_forget()
    app.frame_pcf = FramePcf(app, cod) 
    app.frame_pcf.pack()

def mostrar_pagina_principal(app):
    app.title("Sistema Manutenção")
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
    app.frame_adm.pack_forget()
    app.frame_login.pack_forget()
    app.frame_pcf.pack_forget()
    app.frame_lotto.pack_forget()
    app.frame_descanso.pack_forget()
    app.frame_aprovarlotto.pack_forget()
    app.frame_principal.pack()

def mostrar_pagina_descanso(app):
    app.title("Tela em Construção")
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
    app.frame_adm.pack_forget()
    app.frame_pcf.pack_forget()
    app.frame_login.pack_forget()
    app.frame_lotto.pack_forget()
    app.frame_principal.pack_forget()
    app.frame_aprovarlotto.pack_forget()
    app.frame_descanso.pack()

def mostrar_pagina_lotto(app, modal,usuario, maquina):
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
    app.frame_adm.pack_forget()
    data_atual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    app.frame_login.pack_forget()
    app.frame_descanso.pack_forget()
    app.frame_principal.pack_forget()
    app.frame_aprovarlotto.pack_forget()
    if modal == "Modal":
        janela_lotto_modal = customtkinter.CTk()
        janela_lotto_modal.geometry("{0}x{1}+0+0".format("1050", app.winfo_screenheight()))
        janela_lotto_modal.title("Lotto Modal")

        frame_lotto_modal = FrameLotto(janela_lotto_modal, modal, usuario, maquina, data_atual)
        frame_lotto_modal.pack()

        janela_lotto_modal.protocol("WM_DELETE_WINDOW", janela_lotto_modal.destroy)
        janela_lotto_modal.mainloop()
    else:
        app.title("Lotto")
        app.frame_pcf.pack_forget()
        app.frame_lotto = FrameLotto(app, None,  None,  None, data_atual) 
        app.frame_lotto.pack()