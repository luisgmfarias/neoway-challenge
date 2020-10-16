from scrapping import *
from pandas.testing import assert_frame_equal

def test_dataframe():
    uf_dataframe = pd.DataFrame(columns=['id', 'Localidade', 'Faixa de CEP'])

    exp = pd.DataFrame(data = {'id': ['504'], 'Localidade': ['Cornelio Procopio'], 'Faixa de CEP':['86300-000 à 86300-000']})
    actual = append_df('504', 'Cornelio Procopio', '86300-000 à 86300-000')

    assert_frame_equal(actual.reset_index(drop=True), exp.reset_index(drop=True))

def test_scrapping():

    assert get_data(['AC', 'RR']) == 'success'

def test_verifyUF():
    assert verifyUF(['TU', 'LY', 'A']) == False



