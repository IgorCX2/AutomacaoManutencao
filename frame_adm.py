import customtkinter

class FrameAdm(customtkinter.CTkFrame):
    def __init__(self, master, user=None):
        customtkinter.CTkFrame.__init__(self, master, fg_color='transparent')
        title_label = customtkinter.CTkLabel(self, text="ADM", font=("Helvetica", 70, "bold"), fg_color='transparent', text_color='white')
        title_label.pack(pady=90)
        buttons_nome=["Aprovação Lotto"]
        buttons_comand=[self.ir_para_aprovarlotto,]
        button_frame = customtkinter.CTkFrame(self, fg_color='transparent')
        button_frame.pack(pady=20)
        for i in range(len(buttons_nome)):
                button = customtkinter.CTkButton(button_frame,command=lambda arg=user: buttons_comand[i](arg),  text=buttons_nome[i], width=153, height=120, font=("Helvetica", 18, "bold"), fg_color='white', text_color='dark blue')
                button.pack(side='left', padx=8, pady=8)
        
    def ir_para_aprovarlotto(self, user):
        self.master.mostrar_aprovarlotto(user)