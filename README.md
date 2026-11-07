# SauceDemo Selenium Automation

## Project Overview
This project contains automated UI tests for the SauceDemo demo e-commerce website using Python and Selenium WebDriver.

## Technologies Used
- Python
- Selenium WebDriver
- Google Chrome
- Visual Studio Code

## Automated Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| AT001 | Valid user login | User successfully reaches Products page |
| AT002 | Complete checkout | Order confirmation is displayed |
| AT003 | Locked-out user login | Login is blocked with an error message |

## Project Structure

```text
SauceDemo_Automation/
├── tests/
│   ├── test_login.py
│   ├── test_checkout.py
│   └── test_locked_user.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

1. Clone this repository.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the automated tests:

```bash
python3 tests/test_login.py
python3 tests/test_checkout.py
python3 tests/test_locked_user.py
```

## Test Website
https://www.saucedemo.com/

## Test Credentials
- Standard user: `standard_user`
- Locked-out user: `locked_out_user`
- Password: `secret_sauce`

## Author
QA Engineer Internship Assignment
