*** Settings ***
Documentation    Suite description
library  Selenium2Library
Resource          opencart.robot
Test Setup        Open Opencart Login Page
Test Teardown     Close browser
*** Variables ***
${USER_NAME}    demo
${PASSWORD}     demo


*** Test Cases ***
#Тест открывает продукты в каталоге под админом и ищем все продукты apple
The admin open catalog->products and find products name apple
    Authenticate  ${USER_NAME}    ${PASSWORD}
    Open catalog
    sleep  2s
    Open products
    Input text      id:input-name   Apple
    Click filter


#Тест открывает продукты в каталоге под админом и ищем количество Canon EOS 5D
The admin open catalog->products find count product in list
    Authenticate  ${USER_NAME}    ${PASSWORD}
    Open catalog
    sleep  2s
    Open products
    sleep  1s
    ${count} =  Get Element Count  xpath:*//td[text()='Canon EOS 5D']
    Should Be True	${count} == 1


#Тест открывает продукты в каталоге под админом и копируем элемент
The admin open catalog->products find product and copy
    Authenticate  ${USER_NAME}    ${PASSWORD}
    Open catalog
    sleep  2s
    Open products
    sleep  1s
    Click Element   css:input[type='checkbox'][value ='40']
    Click Element   css:button[data-original-title='Copy']

