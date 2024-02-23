import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Adiciona opção de rodar em Background
option = webdriver.ChromeOptions()
# option.add_argument('--headless=none')
option.add_argument('--start-maximized')

# Inicializa o webdriver do Chrome
driver = webdriver.Chrome(options=option)

# Escolha algo para pesquisar no google
search = 'Extra'

# Abre o endereço no Chrome
driver.get(f'https://www.google.com.br/search?q={search}')
try:
    # Clica no primeiro link
    driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()
    # Vai até a barra de search
    time.sleep(1)
    searchBars = driver.find_elements(By.TAG_NAME, 'input')
    for x in searchBars:
        print(x.get_attribute('outerHTML'))
        if x.get_attribute('id') and 'search' in x.get_attribute('id') :
            x.click()
            x.send_keys("quest 2")
            x.send_keys(Keys.ENTER)
    # searchBar.click()
    # searchBar.send_keys("quest 2")
    # searchBar.send_keys(Keys.ENTER)
    
    # Faz com que o driver espere até uma certa condição
    wait = WebDriverWait(driver, 10)
    # html = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'html'))).get_attribute('outerHTML')
    # soup = BeautifulSoup(html, "html.parser")
    # print(soup.prettify)
    
finally:
    # Fecha o Chrome
    time.sleep(5)
    driver.quit()