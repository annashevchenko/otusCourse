import pytest

"""В тестах необходимо использовать все виды фикстур (session, module, function)"""


@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\n Открываю новую сессию  {request.scope} и начинаю запуск тестов по ДЗ № 3")

    def fin():
        print(f"\n Закрываю сесссию {request.scope} завершаю прогон тестов по ДЗ № 3")
    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\n Выполняем эту фикстуру {request.scope} для каждого модуля в ДЗ № 3")

    def fin():
        print(f"\n Заканчили выоплнять фикстуру  {request.scope} для каждого модуля в ДЗ № 3")
    request.addfinalizer(fin)


@pytest.fixture(scope="class")
def class_fixture(request):
    print(f"\n Выполняем эту фикстуру {request.scope} для каждого класса в ДЗ № 3")

    def fin():
        print(f"\n Заканчили выоплнять фикстуру {request.scope} для каждого класса в ДЗ № 3")
    request.addfinalizer(fin)


@pytest.fixture()
def function_fixture(request):
    print(f"\n Выполняем эту фикстуру {request.scope} для каждой функции в ДЗ № 3")

    def fin():
        print(f"\n Заканчили выоплнять фикстуру {request.scope} для каждой функции в ДЗ № 3")
    request.addfinalizer(fin)