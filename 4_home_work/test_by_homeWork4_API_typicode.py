import pytest


@pytest.mark.parametrize('output_id', [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])])
def test_api_one_typicode_all_users(api_client, output_id):
    """Description: тест по домашнему заданию № 4 api:  https://jsonplaceholder.typicode.com/. запрос на список пользователей,
    """
    res = api_client.get(path="/users").json()
    # Проверяем что возвращаемые параметры верны
    i = 0
    user_id = []
    for res[i] in res:
        for key, value in res[i].items():
            if key == 'id':
                user_id.append(res[i].get(key))
    # Проверяем что возвращаемые параметры верны
    assert user_id == output_id


@pytest.mark.parametrize('input_id, output_id, output_userId, output_title', [
    ('4', 4, 1, 'eum et est occaecati'),
    ('35', 35, 4, 'id nihil consequatur molestias animi provident')])
def test_api_two_typicode_posts_id(api_client, input_id, output_id, output_userId, output_title):
    """Description: тест по домашнему заданию № 4 api:  https://jsonplaceholder.typicode.com/. запрос на сообщение по id"""
    res = api_client.get(path="/posts/" + input_id).json()
    # Проверяем что возвращаемые параметры верны
    assert res['id'] == output_id
    assert res['userId'] == output_userId
    assert res['title'] == output_title



@pytest.mark.parametrize('input_postId, output_id, output_name', [
    ('44', [216, 217, 218, 219, 220], ['voluptatem esse sint alias', 'eos velit velit esse autem minima voluptas',
                                       'voluptatem qui deserunt dolorum in voluptates similique et qui',
                                       'qui unde recusandae omnis ut explicabo neque magni veniam',
                                       'vel autem quia in modi velit'])])
def test_api_three_typicode_posts_id(api_client, input_postId, output_id, output_name):
    """Description: тест по домашнему заданию № 4 api:  https://jsonplaceholder.typicode.com/. запрос на комментарии к посту
     по id поста"""
    res = api_client.get(path="/comments",
                         params={'postId': input_postId}).json()
    # Проверяем что возвращаемые параметры верны
    i = 0
    ids = []
    names = []
    for res[i] in res:
        for key, value in res[i].items():
            if key == 'id':
                ids.append(res[i].get(key))
            if key == 'name':
                names.append(res[i].get(key))
    # Проверяем что возвращаемые параметры верны
    assert ids == output_id
    assert names == output_name




@pytest.mark.parametrize('input_id, input_title',
                         [(663773, 'this test title')])
@pytest.mark.parametrize('output_id, output_title',
                         [('663773', 'this test title')])
def test_api_four_create_resource(api_client, input_id, output_id, input_title, output_title):
    """Description: тест по домашнему заданию № 4 api:  https://jsonplaceholder.typicode.com/. создание нового ресурса
         по id поста"""
    res = api_client.post(
        path="/posts",
        data={'title': input_title,
              'body': 'bar',
              'userId': input_id
              }).json()
    assert res['title'] == output_title
    assert res['body'] == 'bar'
    assert res['userId'] == output_id



@pytest.mark.parametrize('output_id', [
    (100)])
def test_api_five_typicode_all_albums(api_client, output_id):
    """Description: тест по домашнему заданию № 4 api:  https://jsonplaceholder.typicode.com/. запрос на все альбомы
    проверяем колисество полученных записей,
    """
    res = api_client.get(path="/albums").json()
    # Проверяем что возвращаемые параметры верны
    i = 0
    count = 0
    for res[i] in res:
        for key, value in res[i].items():
            if key == 'id':
                count += 1
    # Проверяем что возвращаемые параметры верны
    assert count == output_id