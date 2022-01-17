
from selenium import webdriver  ## simular o uso do navegador atraves da automação web
import time  # aguadar alguns segundos para que possa escanear a tela do computador usando o celular 
from webdriver_manager.chrome import ChromeDriverManager  # simular o uso do navegador sem ferramentas adicionais
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
contacts = ['grupo_zap1','grupo_zap2','grupo_zap3','grupo_zap4','grupo_zap5','grupo_zap6','grupo_zap7']
message = 'BA NOITI :))'



def search_contact(contacts):
    field_research = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    field_research.click()
    field_research.send_keys(contacts) 
    field_research.send_keys(Keys.ENTER)


def send_message(message):
    message_field = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    message_field[1].click()
    time.sleep(3)
    message_field[1].send_keys(message)
    message_field[1].send_keys(Keys.ENTER)



for contact in contacts:
    search_contact(contact) 
    send_message(message)