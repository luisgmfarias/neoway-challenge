from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path=r"driver/chromedriver")
search_page="http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm"

driver.get(search_page)

uf_list=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
selected_ufs = ['BA', 'CE','GO','MA', 'MG', 'PB','PE','PI','PR','RS','SC','SP']

for option in selected_ufs:
    driver.find_element_by_xpath("//select[@name='UF']/option[text()='" + option + "']").click()
    driver.find_element_by_xpath('//*[@id="Geral"]/div/div/div[4]/input').click()
    table = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]').text
    print(table)

    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/a').click() #return to the search page

def pagination():
    return 0



