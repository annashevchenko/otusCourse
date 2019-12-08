*** Settings ***
Documentation    Suite description
library  Selenium2Library

*** Variables ***
${URL}            http://localhost/admin
${BROWSER}        Chrome


*** Test Cases ***
#Тест открывает продукты в каталоге под админом и ищем все продукты apple
The admin open catalog->products and find products name apple
    Open browser    ${URL}  ${BROWSER}
    Maximize Browser Window
    Input text      id:input-username   user
    Input text      id:input-password   bitnami1
    Click Button    css:button[type='submit']
    Click Element   css:li[id='menu-catalog']
    sleep  2s
    Click Element   xpath=*//a[text()='Products']
    Input text      id:input-name   Apple
    Click Button    css:button[id='button-filter']
    Close browser


##Тест открывает продукты в каталоге под админом и ищем количество Canon EOS 5D
The admin open catalog->products find count product in list
    Open browser    ${URL}  ${BROWSER}
    Maximize Browser Window
    Input text      id:input-username   user
    Input text      id:input-password   bitnami1
    Click Button    css:button[type='submit']
    Click Element   css:li[id='menu-catalog']
    sleep  1s
    Click Element   xpath=*//a[text()='Products']
    sleep  1s
    ${count} =  Get Element Count  xpath:*//td[text()='Canon EOS 5D']
    Should Be True	${count} == 1
    Close browser



#Тест открывает продукты в каталоге под админом и копируем элемент
The admin open catalog->products find product and copy
    Open browser    ${URL}  ${BROWSER}
    Maximize Browser Window
    Input text      id:input-username   user
    Input text      id:input-password   bitnami1
    Click Button    css:button[type='submit']
    Click Element   css:li[id='menu-catalog']
    sleep  1s
    Click Element   xpath=*//a[text()='Products']
    sleep  1s
    Click Element   css:input[type='checkbox'][value ='40']
    Click Element   css:button[data-original-title='Copy']

    Close browser

