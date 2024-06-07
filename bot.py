import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

username = ""
password = ""

def realizar_login():
    driver.get("https://instagram.com")
    time.sleep(5)  
    
    input_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
  
    time.sleep(1)
    input_password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
 
    time.sleep(1)
    button_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

    time.sleep(10) 

def contatos_aleatorios():
    contatos = ["@alcantaraabia", "@mariajosechitarrelli", "@manoellourenco10", "@katiachitarrelli", "@rebelothiago", "@anselmocarvalho_", "@alcantaramaju25", "@nathaliafm7", "@juliaastuart", "@lcmariano__", "@deborahhalcantara", "@chitarrelli_kt"]
    contatos_selecionados = random.sample(contatos, 3)
    return " ".join(contatos_selecionados)

def enviar_mensagem():
    contatos_selecionados = contatos_aleatorios()
    mensagem = "#magodasmilhas #queroserummilionariodemilhas #fabricademilhas " + contatos_selecionados
    time.sleep(10)
    marcar_contatos = driver.find_element(By.CLASS_NAME, 'x1qlqyl8').send_keys(mensagem)
    time.sleep(60)  
    button_enviar = driver.find_element(By.XPATH, '//div[contains(text(), "Post")]').click()
    time.sleep(10)
  
realizar_login()

driver.get("https://www.instagram.com/p/C72tW2GICaN/")
time.sleep(5) 

input_post = driver.find_element(By.CLASS_NAME, 'x1qlqyl8').click()
time.sleep(2)

for i in range(200):  
    enviar_mensagem()
    print(f"Mensagem {i+1} enviada")

driver.quit()

