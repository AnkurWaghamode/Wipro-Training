*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${URL}        https://example.com
${TITLE}      Example Domain

*** Test Cases ***
Open Website And Verify Title
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    ${TITLE}
    Capture Page Screenshot
    Close Browser
