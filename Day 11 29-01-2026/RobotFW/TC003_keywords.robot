*** Settings ***
Library    SeleniumLibrary

***Keywords ***
Open application
     Open Browser    https://www.google.com    chrome
     maximize browser window



*** Test Cases ***
TC002.robot
Open application
    Title Should Be    Google
    Close Browser
