import pytest



@pytest.mark.parametrize('param,  output_name, type, street, city, phone', [
    ('patio', 'MadTree Brewing', 'regional', '3301 Madison Rd', 'Cincinnati', '5138368733')])
def test_api_one_breweries_by_tag(api_client, param, output_name, type, street, city, phone):
    """Description: тест по домашнему заданию № 4 api: https://api.openbrewerydb.org запрос c фильтром по тегу,
     проверяем, что возвращается верные данные"""
    res = api_client.get(path="/breweries",
                         params={'by_tag': param}).json()
    # Проверяем что возвращаемые параметры верны
    res = res[0]
    assert res['name'] == output_name
    assert res['brewery_type'] == type
    assert res['street'] == street
    assert res['city'] == city
    assert res['phone'] == phone


@pytest.mark.parametrize('param1, param2, output_id', [
    ('cooper', 'new_york', [4674, 4675]),
    ('cvdbdr', 'new_york', []),
    ('', '', [2, 4, 44, 46, 55, 76, 94, 98, 104, 107, 127, 141, 163, 182, 187, 198, 219, 225, 235, 247])])
def test_api_two_breweries_byName_byState(api_client, param1, param2, output_id):
    """Description: тест по домашнему заданию № 4 api: https://api.openbrewerydb.org запрос по пивоварням с параметрами имя и штат
    проверяем, что возвращаются верные id"""
    res = api_client.get(
        path="/breweries/",
        params={'by_name': param1,
                'by_state': param2
                }).json()
    i = 0
    breweries_id = []
    for res[i] in res:
        for key, value in res[i].items():
            if key == 'id':
                breweries_id.append(res[i].get(key))
    # Проверяем что возвращаемые параметры верны
    assert breweries_id == output_id


@pytest.mark.parametrize('input_id, output_name, output_code', [
    ('127', 'Dragoon Brewing Co', '85745-1214'),
    ('104', 'BJs Restaurant & Brewery - Chandler', '85226-5175')])
def test_api_three_breweries_by_Id(api_client, input_id, output_name, output_code):
    """Description: тест по домашнему заданию № 4 api: https://api.openbrewerydb.org запрос id пивоварни
    проверяем, что возвращаются верные данные: имя и почтовый индекс"""
    res = api_client.get(
        path="/breweries/" + input_id
    ).json()
    # Проверяем что возвращаемые параметры верны
    assert res['name'] == output_name
    assert res['postal_code'] == output_code


@pytest.mark.parametrize('param1, output_name, output_street', [
    ('Band of Brothers', 'Band of Brothers Brewing Company', '1605 23rd Ave')])
def test_api_four_breweries_search(api_client, param1, output_name, output_street):
    """Description: тест по домашнему заданию № 4 api: https://api.openbrewerydb.org запрос на поиск пивоварни
    проверяем, что возвращаются верные данные: имя и адрес"""
    res = api_client.get(
        path="/breweries/search",
        params={'query': param1
                }).json()
    res = res[0]
    # Проверяем что возвращаемые параметры верны
    assert res['name'] == output_name
    assert res['street'] == output_street


@pytest.mark.parametrize('param1, param2, output_id', [
    ('micro', 'Cleveland', [5383, 5365, 5450, 5502, 5503, 5549, 5603, 5605, 5610, 5646]),
    ('planning', 'Cleveland', [2202, 5358, 5590]),
    ('54564', 'Cleveland', [])])
def test_api_five_breweries_by_type_by_city(api_client, param1, param2, output_id):
    """Description: тест по домашнему заданию № 4 api: https://api.openbrewerydb.org запрос по пивоварням с параметрами тип и город
    проверяем, что возвращаются верные id"""
    res = api_client.get(
        path="/breweries/",
        params={'by_type': param1,
                'by_city': param2
                }).json()
    i = 0
    breweries_id = []
    for res[i] in res:
        for key, value in res[i].items():
            if key == 'id':
                breweries_id.append(res[i].get(key))
    # Проверяем что возвращаемые параметры верны
    assert breweries_id == output_id
