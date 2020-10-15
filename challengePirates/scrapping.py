from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
import time
import uuid
import sys

# Setting webdriver headless option
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Initiating chrome webdriver
driver = webdriver.Chrome(executable_path=r"driver/chromedriver")

# # BuscaCep page navigation
search_page = "http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm"
driver.get(search_page)

# all UFs
UFs = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT',
       'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

# initiating pandas dataframe
uf_dataframe = pd.DataFrame(columns=['id', 'Localidade', 'Faixa de CEP'])


def get_data(uf_list):

    for option in uf_list:
        # selecting UF option on drop down menu
        driver.find_element_by_xpath(
            "//select[@name='UF']/option[text()='" + option + "']").click()
        driver.find_element_by_xpath(
            '//*[@id="Geral"]/div/div/div[4]/input').click()

        # find table
        table = driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]')

        pagination(table)

        # time delay
        time.sleep(2)
        # return to the search page
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/a').click()

    return 'success'


def pagination(table):

    # running through all table pages
    for row in table.find_elements_by_tag_name('tr')[2:]:
        city = row.find_element_by_xpath('./td[1]')
        cep_range = row.find_element_by_xpath('./td[2]')
        append_df(uuid.uuid4().int, city.text, cep_range.text)

    # try-except to verify if button 'Proxima' (next page) is clickable or not
    # this is important to check if it is the last page
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/a').click()
    except WebDriverException:
        return 0

    # recursiveness
    pagination(driver.find_element_by_class_name('tmptabela'))


def append_df(id, city, cep_range):
    global uf_dataframe
    # adding a row to our dataframe
    uf_dataframe = uf_dataframe.append(
        [{'id': id, 'Localidade': city, 'Faixa de CEP': cep_range}], ignore_index=True)

    return uf_dataframe


def verifyUF(args):
    for uf in args:
        if uf not in UFs:
            print('arguments {} are not properly set '.format(args))
            return False
    return True


def main():

    if len(sys.argv) > 1:
        if (verifyUF(sys.argv[1:])):
            get_data(sys.argv[1:])
    else:
        # if dont have any args, will scrapy DF, ES, GO, MA
        get_data(UFs[6:10])

    driver.close()

    # generating jsonl output
    uf_dataframe.to_json(r'./output.jsonl', orient='records',
                         lines=True, force_ascii=False)


if __name__ == '__main__':
    main()
