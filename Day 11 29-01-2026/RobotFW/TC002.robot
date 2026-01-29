*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
TC001
   Log    Test started
Open Google
    Open Browser    https://www.google.com    chrome
    Title Should Be    Google
    Close Browser
