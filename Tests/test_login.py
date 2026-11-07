
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():

    # Start Chrome browser
    driver = webdriver.Chrome()

    try:
        # Open SauceDemo website
        driver.get("https://www.saucedemo.com/")

        # Maximize browser
        driver.maximize_window()

        # Wait for username field
        wait = WebDriverWait(driver, 10)

        # Enter username
        username = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("standard_user")

        # Enter password
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        # Click login button
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Verify successful login
        wait.until(
            EC.url_contains("inventory.html")
        )

        # Verify Products heading
        heading = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        assert heading.text == "Products"

        print("TEST PASSED: Valid login successful")

    except Exception as error:
        print("TEST FAILED:", error)
        raise

    finally:
        # Close browser
        driver.quit()


if __name__ == "__main__":
    test_valid_login()
