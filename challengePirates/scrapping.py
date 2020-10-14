from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
import time
import uuid

# Setting webdriver headless option
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Initiating chrome webdriver
driver = webdriver.Chrome(executable_path=r"driver/chromedriver")

# BuscaCep page navigation
search_page = "http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm"
driver.get(search_page)

# all UFs
UFs = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT',
       'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']


def get_data(uf_list):

    for option in uf_list:
        driver.find_element_by_xpath(
            "//select[@name='UF']/option[text()='" + option + "']").click()
        driver.find_element_by_xpath(
            '//*[@id="Geral"]/div/div/div[4]/input').click()
        table = driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]')

        pagination(table)

        time.sleep(2)
        # return to the search page
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/a').click()


def pagination(table):

    for row in table.find_elements_by_tag_name('tr')[2:]:
        city = row.find_element_by_xpath('./td[1]')
        cep_range = row.find_element_by_xpath('./td[2]')
        insert_data(uuid.uuid4().int, city.text, cep_range.text)

    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/a').click()
    except WebDriverException:
        return 0

    pagination(driver.find_element_by_class_name('tmptabela'))


def insert_data(id, city, cep_range):
    global uf_dataframe
    uf_dataframe = uf_dataframe.append(
        [{'id':id, 'Localidade': city, 'Faixa de CEP': cep_range}], ignore_index=True)
    return 0


if __name__ == "__main__":
    uf_dataframe = pd.DataFrame(columns=['id','Localidade', 'Faixa de CEP']) #initiating pandas dataframe
    get_data(UFs[5:6]) #scrapping first four UFs in alphabetical order
    print(uf_dataframe)
