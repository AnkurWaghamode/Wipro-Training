*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=C:/Users/91861/PycharmProjects/pythonProject8/RobotFW/testdata.xlsx
Test Template    OrangeHRM Login With Excel


*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   firefox

*** Keywords ***


OrangeHRM Login With Excel
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Sleep    3s
    Capture Page Screenshot
    Click Button    xpath=//button[@type='submit']
    Sleep    3s
    Capture Page Screenshot
    click image    xpath=//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/img
    click link    linktext=Logout
    Close Browser

*** Test Cases ***
TC006_DDExcel_Login
