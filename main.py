import sys
import os
import numpy as np

"""# Configuração do Web-Driver"""
# Utilizando o WebDriver do Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Instanciando o Objeto ChromeOptions
options = webdriver.ChromeOptions()

# Passando algumas opções para esse ChromeOptions
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-crash-reporter')
options.add_argument('--log-level=3')
options.add_argument('--disable-gpu')


# Criação do WebDriver do Chrome
wd_Chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

"""# Importando as Bibliotecas"""

import pandas as pd
import time
from tqdm import tqdm

"""# Iniciando a Raspagem de Dados"""

# Com o WebDrive a gente consegue a pedir a página (URL)
wd_Chrome.get("https://www.flashscore.com.br/basquete/eua/nba/resultados/") 
time.sleep(2)

#Abrir aba resultados
#resultados = wd_Chrome.find_elements(By.CSS_SELECTOR, 'div.tabs__tab results selected')
#wd_Chrome.execute_script("arguments[0].click();", resultados)
#time.sleep(2)

#Selecionar resultados

#coletar dados
dados = {
    "HOME":[],
    "AWAY":[],
    "FTH":[],
    "FTA":[],
    "PQH":[],
    "PQA":[],
    "SQH":[],
    "SQA":[],
    "TQH":[],
    "TQA":[],
    "QQH":[],
    "QQA":[],
    "EQH":[],
    "EQA":[],
}

count = 0
eventos = wd_Chrome.find_elements(By.CSS_SELECTOR, 'div.event__match')
for evento in eventos:
    try:
        count +=1
        home = evento.find_element(By.CSS_SELECTOR, 'div.event__participant--home').text
        away = evento.find_element(By.CSS_SELECTOR, 'div.event__participant--away').text
        fth = evento.find_element(By.CSS_SELECTOR, 'div.event__score--home').text
        fta = evento.find_element(By.CSS_SELECTOR, 'div.event__score--away').text
        pqh = evento.find_element(By.CSS_SELECTOR, 'div.event__part--home.event__part--1').text
        pqa = evento.find_element(By.CSS_SELECTOR, 'div.event__part--away.event__part--1').text
        sqh = evento.find_element(By.CSS_SELECTOR, 'div.event__part--home.event__part--2').text
        sqa = evento.find_element(By.CSS_SELECTOR, 'div.event__part--away.event__part--2').text
        tqh = evento.find_element(By.CSS_SELECTOR, 'div.event__part--home.event__part--3').text
        tqa = evento.find_element(By.CSS_SELECTOR, 'div.event__part--away.event__part--3').text
        qqh = evento.find_element(By.CSS_SELECTOR, 'div.event__part--home.event__part--4').text
        qqa = evento.find_element(By.CSS_SELECTOR, 'div.event__part--away.event__part--4').text
        eqh = evento.find_element(By.CSS_SELECTOR, 'div.event__part--home.event__part--5').text
        eqa = evento.find_element(By.CSS_SELECTOR, 'div.event__part--away.event__part--5').text

        print(f'Evento: {home} {fth} x {fta} {away}')
        dados["HOME"].append(home)
        dados["AWAY"].append(away)
        dados["FTHG"].append(fth)
        dados["FTAG"].append(fta)
        dados["PQH"].append(pqh)
        dados["PQA"].append(pqa)
        dados["SQH"].append(sqh)
        dados["SQA"].append(sqa)
        dados["TQH"].append(tqh)
        dados["TQA"].append(tqa)
        dados["QQH"].append(qqh)
        dados["QQA"].append(qqa)
        dados["EQH"].append(eqh)
        dados["EQA"].append(eqa)

    except Exception as error:
        print(f'Evento: {home} {fth} x {fta} {away}\nErro: {error}')
        pass
print(f'{count} jogos.')

df = pd.DataFrame(dados)
filename = "datasetnbaa.csv"
df.to_csv(filename, sep=";", index=False)