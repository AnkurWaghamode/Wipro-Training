*** Settings ***
Library         SeleniumLibrary
Library         DataDriver    file=login_data.csv
Test Template   Login Test Template

*** Variables ***
${BROWSER}      chrome
${URL}          https://example.com/login

*** Test Cases ***
Login Test Using CSV Data
# ⚠️ NO arguments, NO steps here

*** Keywords ***
# ---------- Keyword-Driven Keywords ----------
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Close Application
    Close Browser

Enter Credentials
    [Arguments]    ${username}    ${password}
    Input Text     id=username    ${username}
    Input Text     id=password    ${password}
    Click Button   id=login

Verify Login Result
    [Arguments]    ${expected_result}
    Run Keyword If    '${expected_result}' == 'PASS'
    ...    Page Should Contain    Dashboard
    Run Keyword If    '${expected_result}' == 'FAIL'
    ...    Page Should Contain    Invalid credentials

# ---------- Data-Driven Template ----------
Login Test Template
    [Arguments]    ${username}    ${password}    ${expected_result}
    Open Application
    Enter Credentials    ${username}    ${password}
    Verify Login Result  ${expected_result}
    Capture Page Screenshot
    Close Application
