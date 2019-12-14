*** Variables ***
${URL}          https://demo.opencart.com/admin/
${BROWSER}      chrome

*** Keywords ***
Open Opencart Login Page
    Headless Chrome - Open Browser

Headless Chrome - Open Browser
    ${chrome_options} =     Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}   add_argument    headless
    Call Method    ${chrome_options}   add_argument    disable-gpu
    ${options}=     Call Method     ${chrome_options}    to_capabilities
    Open Browser    ${URL}    browser=${BROWSER}        desired_capabilities=${options}
    Set Window Size     1920    1200

Input username
    [Arguments]    ${username}
    Input text      id:input-username   ${username}

Input password
    [Arguments]    ${password}
    Input text      id:input-password   ${password}

Click login
    Click Button    css:button[type='submit']

Open catalog
    Click Element   css:li[id='menu-catalog']

Open products
    Click Element   xpath=*//a[text()='Products']

Click filter
    Click Button    css:button[id='button-filter']

Authenticate
    [Arguments]     ${login}    ${secret}
    Input username  ${login}
    Input password  ${secret}
    Click login
