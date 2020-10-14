from scrapping import get_data, driver_init
from selenium import webdriver

def test_driver():
    driver = webdriver.Chrome(executable_path=r"driver/chromedriver")
    assert driver_init() == driver.get('http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm')

