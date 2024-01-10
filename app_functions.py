import time
import requests
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions_share import carregar_maquina, buscar_maquina_nome

def reiniciar_temporizador(app, event):
    app.tempo_inativo = time.time()

def acessar_pcFactory():
    print("ACESSAR API")
    maquinaLista = carregar_maquina()
    url = "http://10.36.216.25:9095/maps/v1"
    response = requests.get(url)

    if response.status_code == 200:
        dados_api = response.json()
        resultados = []

        for item in dados_api:
            local = item.get("name")
            for maquinas in item["resources"]:
                maquina = maquinas.get("code")
                cod = maquinas.get("statusCode")
                if cod == "0409":
                    resultado = maquina
                    maquinaInfo = buscar_maquina_nome(maquina, maquinaLista)
                    print(maquinaInfo)
                    servico = webdriver.ChromeService()
                    navegador = webdriver.Chrome(service=servico)
                    navegador.get("http://10.36.216.25:9097") #entrar no site
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')) #escrever no login
                    ).send_keys('31231')
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')) #escrever no login
                    ).send_keys('31231')
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-authentication/div/div/div/div[2]/form/app-button[1]/button'))
                    ).click()
                    time.sleep(2)
                    navegador.get("http://10.36.216.25:9097/screens/A0028")
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="resource-status"]')) #escrever no login
                    ).send_keys(maquina)
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop"]/div/div[1]/div/span'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop"]/div/div[2]/app-input-date-picker/div/form/div/app-button/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop"]/div/div[2]/app-input-date-picker/div/form/lib-angular-mydatepicker-calendar/div/div/lib-footer-bar/div/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-filter"]/button'))
                    ).click()
                    element = WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-home/div/main/app-screens-page/app-dyn-page/app-a0028/div/app-a0028-edit-status-resource/div[3]'))
                    )
                    entries = element.find_elements(By.XPATH, './div')
                    if entries:
                        last_entry = entries[-1]
                        last_entry_text = last_entry.find_element(By.XPATH, './div/div[2]/div[3]/ppi-field/div/div').text
                        print(last_entry_text)
                    else:
                        print("Nenhuma entrada encontrada")

    else:
        print(f"Falha na requisição. Código de status: {response.status_code}")
def Temporizador(app):
    app.after(1000, lambda: Temporizador(app))
    #app.temporizador_contador+=1
    #if(app.temporizador_contador == 15):
        #acessar_pcFactory()
        #app.temporizador_contador=0
    if time.time() - app.tempo_inativo > 5:
        if(app.pagina_ativa == "descanso"):
            return 0
        app.navigate_to_page("descanso", None)
        return 0
    elif app.pagina_ativa != "descanso":
        return 0
    else:
        app.navigate_to_page("home", None)
        return 0
