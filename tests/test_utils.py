from utils import get_filtered_data, formatted_data


def test_formatted_data(data_oper):
    assert formatted_data(data_oper) == [
        '26.08.2019 Перевод организации\nMaestro 1596837** **** 5199 -> Счет ** 9589\n31957.58 руб.',
        '03.07.2019 Перевод организации\nMasterCard 7158300** **** 6758 -> Счет ** 5560\n8221.37 USD',
        '30.06.2018 Перевод организации\nСчет ** 6952 -> Счет ** 6702\n9824.07 USD',
        '23.03.2018 Открытие вклада\nСчет ** 2431\n48223.05 руб.']


def test_filtered_data(data_oper):
    data = get_filtered_data(data_oper)
    assert len(data) == 4
