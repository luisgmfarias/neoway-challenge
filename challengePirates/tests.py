from scrapping import get_data, driver_init
from selenium import webdriver
import pandas as pd

def init_dataframe():
    uf_dataframe = pd.DataFrame(columns=['id', 'Localidade', 'Faixa de CEP'])

def test_driver():
    driver = webdriver.Chrome(executable_path=r"driver/chromedriver")
    assert driver_init() == driver.get('http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm')

