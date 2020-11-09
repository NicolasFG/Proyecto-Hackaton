from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from re import split
import time
from timeit import default_timer


primero = True
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def validar_nombre(nombre):
    total = nombre.count(' ')
    if total < 1:
        print("No conforme")
        return False;
    print("Conforme")
    return True


def validar_observaciones(texto):
    numero = split('\D+', texto)
    for i in numero:
        if len(i) == 7 or len(i) == 9:
            print("Conforme")
            return True
    print("No conforme")
    return False


def login_plataforma(usuario, contrasena):
    driver.implicitly_wait(5)
    driver.get("https://login.etadirect.com/telefonica-pe.etadirect.com/mobility")
    driver.maximize_window()

    time.sleep(1)
    username = driver.find_element_by_id("username")
    username.send_keys(usuario)
    time.sleep(1)

    password = driver.find_element_by_id("password")
    password.send_keys(contrasena)
    time.sleep(1)
    password.send_keys(Keys.RETURN)

    try:
        checkbox = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='checkbox-mark']"))
        )
        checkbox.click()
        password = driver.find_element_by_id("password")
        password.send_keys(contrasena)
        time.sleep(1)
        password.send_keys(Keys.RETURN)
    except:
        pass


def buscar_formulario(id_formulario):
    inicio = default_timer()
    try:
        global primero
        if primero == True:
            search_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='jbf-container']/div"))
            )
            search_button = search_button.find_element_by_tag_name("app\:header")
            search_button = search_button.find_element_by_tag_name("services\:global\-search\:global\-search\-button")
        else:
            search_button = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='action-global-search']"))
            )
        search_button.click()

        if primero == False:
            clearbutton = driver.find_element_by_xpath("//div[@id='search-bar-container']/div[2]/div/div[2]")
            clearbutton.click()

        search_bar = driver.find_element_by_xpath("//div[@id='search-bar-container']/div[2]/div/div[4]/div")
        search_bar.click()


        search_bar = driver.find_element_by_xpath("//div[@id='search-bar-container']/div[2]/div/div[4]/input")
        search_bar.send_keys(id_formulario)

        search_bar.send_keys(Keys.RETURN)

        results = driver.find_elements_by_xpath(
            "//div[@id='search-bar-container']/div[5]/oj-collapsible/div[2]/div/div[1]/div")
        for result in results:
            if 'No Realizada' in result.text:
                result.click()
                break
        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//span[@class='cl-static-text' and @data-label='XA_REQUIREMENT_NUMBER']"), id_formulario)
        )
        primero = False
    except:
        driver.quit()
    fin = default_timer()
    Tiempo = fin-inicio
    print("Tiempo funcion Buscar Formulario")
    print(Tiempo)



def validar_campos_formulario():
    inicio = default_timer()
    try:
        name = driver.find_element_by_xpath("//span[@class='cl-static-text' and @data-label='A_RECEIVE_PERSON_NAME']")
        name = name.text

        observation = driver.find_element_by_xpath("//div[@class='cl-static-html' and @data-label='A_OBSERVATION']")
        observation = observation.text

        nombre=validar_nombre(name)
        obs=validar_observaciones(observation)
        rpta=[]
        print("validar")
        if nombre==True:
            rpta.append("Conforme")
        else:
            rpta.append("No Conforme")

        if obs==True:
            rpta.append("Conforme")
        else:
            rpta.append("No Conforme")

        return rpta
    except NoSuchElementException:
        driver.quit()
    fin = default_timer()
    Tiempo = fin - inicio
    print("Tiempo validacion Formulario")
    print(Tiempo)


def descargar_fachada():
    try:
        fachada = driver.find_element_by_xpath("//img[@aria-label='Foto Casa del Cliente']")
        fachada = fachada.get_attribute("src")
        print(fachada)
    except NoSuchElementException:
        driver.quit()

def funcion(codes,logeada):
    if logeada==False:
        login_plataforma('HACKATON1', 'Hackaton_1')
    dicc={}
    for code in codes:
        buscar_formulario(str(code))
        aux=validar_campos_formulario()
        dicc[str(code)]=aux
    return dicc


'''
inicio = default_timer()
Recognition('validation/Otros/CINTILLO_155.jpg', "Cintillo")
fin = default_timer()
print(fin-inicio)
 '''

'''
login_plataforma('HACKATON1', 'Hackaton_1')
print("Test 1:")
buscar_formulario('12486764')
validar_campos_formulario()
print("Test 2:")
buscar_formulario('12488495')
validar_campos_formulario()
print("Test 3:")
buscar_formulario('88108038')
validar_campos_formulario()
print("Test 4:")
buscar_formulario('12491276')
validar_campos_formulario()
print("Test 5:")
buscar_formulario('12472502')
validar_campos_formulario()
'''
