from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from re import split
import time

primero = True
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def validar_nombre(nombre):
    total=nombre.count(' ')
    if total<1:
        print("No conforme")
        return False;
    print("Conforme")
    return True

def validar_observaciones(texto):
    numero= split('\D+',texto)
    for i in numero:
        if len(i)==7 or len(i)==9:
            print("Conforme")
            return True
    print("No conforme")
    return False

def login_plataforma(usuario, contraseña):
    
    driver.implicitly_wait(5)
    driver.get("https://login.etadirect.com/telefonica-pe.etadirect.com/mobility")
    driver.maximize_window()
    
    time.sleep(1)
    username = driver.find_element_by_id("username")
    username.send_keys(usuario)
    time.sleep(1)

    password = driver.find_element_by_id("password")
    password.send_keys(contraseña)
    time.sleep(1)
    password.send_keys(Keys.RETURN)

def validar_campos_formulario(id_formulario):
    try:
        global primero
        if primero == True:
            search_button = WebDriverWait(driver,20).until(
                EC.presence_of_element_located((By.XPATH,"//div[@id='jbf-container']/div"))
            )
            search_button = search_button.find_element_by_tag_name("app\:header")
            search_button = search_button.find_element_by_tag_name("services\:global\-search\:global\-search\-button")
        else:
            search_button = WebDriverWait(driver,60).until(
                EC.presence_of_element_located((By.XPATH,"//div[@id='action-global-search']"))
            )
        search_button.click()
        time.sleep(1)
        if primero == False:
            clearbutton = driver.find_element_by_xpath("//div[@id='search-bar-container']/div[2]/div/div[2]")
            clearbutton.click()

        search_bar = driver.find_element_by_xpath("//div[@id='search-bar-container']/div[2]/div/div[4]/div")
        search_bar.click()

        time.sleep(1)
        search_bar = driver.find_element_by_xpath("//div[@id='search-bar-container']/div[2]/div/div[4]/input")
        search_bar.send_keys(id_formulario)
        time.sleep(1)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(1)
        results = driver.find_elements_by_xpath("//div[@id='search-bar-container']/div[5]/oj-collapsible/div[2]/div/div[1]/div")
        for result in results:
            if 'No Realizada' in result.text:
                result.click()
                break
        time.sleep(5)
        name = driver.find_element_by_xpath("//span[@class='cl-static-text' and @data-label='A_RECEIVE_PERSON_NAME']")
        name = name.text

        observation = driver.find_element_by_xpath("//div[@class='cl-static-html' and @data-label='A_OBSERVATION']")
        observation = observation.text

        validar_nombre(name)
        validar_observaciones(observation)

        primero = False

    except:
        driver.quit()

