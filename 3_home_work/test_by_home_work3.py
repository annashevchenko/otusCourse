import pytest
import random
import string


@pytest.fixture
def fixture_create_random_string():
    """эта фикстура создает произвольную строку из строчных и заглавных букв и цифр"""
    string_random = ''.join(
        random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(40))
    return string_random


class TestClass:

    """Description: этот тест № 1 удаляет повторяющиеся символы в строке"""
    def test_one_delete_repeat_symbol_in_string(self, session_fixture, module_fixture, fixture_create_random_string):
        print("Этот тест находит повторяющиеся символы в строке и удаляет их, проверяет,"
              " что длина новой строки равна длине старой строки минус количество повторяющихся символов")
        print("В строке " + fixture_create_random_string + " удаляем повторяющиеся символы")
        new_string_without_repeat = ''
        sum: int = 0
        for i in fixture_create_random_string:
            if i not in new_string_without_repeat:
                new_string_without_repeat += i
            else:
                sum += 1
        print("\nПолучили новую строку: " + new_string_without_repeat)
        print("\nКоличество повторяющихся символов: " + str(sum))
        print("\nВыполняем проверку, что повторяющиеся символы удалились корректно")
        assert (len(new_string_without_repeat) == len(fixture_create_random_string) - sum)

    """Description: этот тест  № 2 считает количество строчных, прописных букв и цифр в строке"""
    def test_two_count_symbol(self, function_fixture, class_fixture, fixture_create_random_string):
        print("Этот тест считает количество строчных, прописных букв и цифр в строке  и проверяет эти значения")
        sum_small_symbol = 0
        sum_big_symbol = 0
        sum_num_symbol = 0
        big_symbol = ''
        small_symbol = ''
        num_symbol = ''
        for i in fixture_create_random_string:
            if 'a' <= i <= 'z':
                sum_small_symbol += 1
                small_symbol += i
            if 'A' <= i <= 'Z':
                sum_big_symbol += 1
                big_symbol += i
            if '0' <= i <= '9':
                sum_num_symbol += 1
                num_symbol += i
        print("\nКоличество строчных символов равно " + str(sum_small_symbol))
        print("\nКоличество прописных символов в равно " + str(sum_big_symbol))
        print("\nКоличество цифр  равно " + str(sum_num_symbol))
        print("\nВыполняем проверку, что количество прописных и строчных символов посчитано верно")
        assert (len(small_symbol) == len(fixture_create_random_string) - sum_big_symbol - sum_num_symbol)
        assert (len(big_symbol) == len(fixture_create_random_string) - sum_small_symbol - sum_num_symbol)
        assert (len(num_symbol) == len(fixture_create_random_string) - sum_big_symbol - sum_small_symbol)

    """Description: этот тест  № 3 сортирует список и проверяет правильность сортировки"""
    def test_three_sort_symbol_in_list(self, function_fixture, class_fixture, module_fixture):
        print("Этот тест сортирует список и проверяем, что сортировка выполнена верна")
        list_before = [1, 2, 56, 43, 89, 23, 3, 5, 4, 1, 78, 89, 4242, 56, 22, 34, 76, 89, 90]
        newList = sorted(list_before)
        print(newList)
        assert (newList == [1, 1, 2, 3, 4, 5, 22, 23, 34, 43, 56, 56, 76, 78, 89, 89, 89, 90, 4242])

    """Description: этот тест  № 4 находит минимальную длину элемента в списке"""
    def test_four_min_lenght_element_in_list(self, function_fixture, class_fixture, module_fixture):
        print("Этот тест находит минимальную длину элемента списка и проверяет его")
        elements = ["xxxxауауxx", "yyваацацy", "zпупупупупу", "cdvdsvertgv"]
        for element in elements:
            min = len(element)
            if len(element) < min:
                min = len(element)
        print(min)
        assert (min == 11)

    """Description: этот тест  № 5  вытаскивает значение из словаря по ключу"""
    def test_five_check_value_by_key(self, class_fixture, module_fixture):
        print("Этот тест вытаскивает значение из словаря по ключу")
        capitals = {'Russia': 'Moscow', 'Brazil': 'Brasilia', 'USA': 'Washington', 'China': 'Beijing',
                    'Hungary': 'Budapest', 'Italy': 'Rome'}
        for key in capitals:
            if key == 'Hungary':
                city = capitals.get(key)
        print(city)
        assert (city == 'Budapest')

    """Description: этот тест  № 6  перебирает словарь и  если значение больше 5 добавляем его в новый список"""
    def test_six__symbol_more_in_list(self, class_fixture, module_fixture):
        print("Этот тест перебирает словарь и  если значение больше 5 добавляем его в новый список")
        dict_old = {1: 15, 2: 3, 3: 2, 4: 4, 5: 3, 6: 67}
        dl = []
        for key, value in dict_old.items():
            if dict_old.get(key) > 5:
                print(dict_old.get(key))
                dl.append(dict_old.get(key))
        print(dl)
        assert (dl == [15, 67])

    """Description: этот тест  № 7  создает кортеж и считает количество элементов n в созданном кортеже"""
    def test_seven__count_element_in_tuple(self, class_fixture, function_fixture):
        print("Этот тест создает кортеж и считает количество элементов l в созданном кортеж")
        a = tuple('One fine evening a young princess put on her bonnet and clogs')
        assert (a.count('n') == 10)

    """Description: этот тест  № 8  создает кортеж и повторяет его 4 раза"""
    def test_eight_repeat_tuple(self, class_fixture, module_fixture):
        print("Этот тест создает кортеж и создает кортеж и повторяет его 4 раза")
        a = tuple('hello')*4
        assert (a == ('h', 'e', 'l', 'l', 'o', 'h', 'e', 'l', 'l', 'o',
                      'h', 'e', 'l', 'l', 'o', 'h', 'e', 'l', 'l', 'o'))

    """Description: этот тест  № 9  объединяет множество из элементов,
    встречающихся в одном множестве, но не встречающиеся в обоих"""
    def test_nine_repeat_tuple(self, function_fixture, module_fixture):
        print("Этот тест объединяет множество из элементов,"
              "встречающихся в одном множестве, но не встречающиеся в обоих")
        a = {1, 32, 2, 5, 6, 89, 23, 43, 12, 56, 71, 3}
        b = {1, 2, 3, 4, 6, 7, 89, 65, 32, 3, 4, 1, 7, 8, 90, 56, 3, 2}
        c = a ^ b
        assert (c == {4, 65, 7, 8, 5, 71, 43, 12, 23, 90})

    """Description: этот тест  № 10  объединяет множества в одно"""
    def test_ten_repeat_tuple(self, class_fixture, session_fixture):
        print("Этот тест объединяет множество  объединяет множества в одно,")
        a = {1, 32, 2, 5, 6, 89, 23, 43, 12, 56, 71, 3}
        b = {1, 2, 3, 4, 6, 7, 89, 65, 32, 3, 4, 1, 7, 8, 90, 56, 3, 2}
        c = a | b
        assert (c == {1, 2, 3, 4, 5, 6, 71, 65, 7, 8, 12, 23, 89, 90, 32, 43, 56})
