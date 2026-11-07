
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Open SauceDemo
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Login
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Wait for Products page
        wait.until(EC.url_contains("inventory.html"))

        # Add Sauce Labs Backpack to cart
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        # Verify cart badge
        cart_badge = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )
        assert cart_badge.text == "1"

        # Open cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verify product in cart
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        # Click Checkout
        driver.find_element(By.ID, "checkout").click()

        # Enter checkout information
        wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Test")

        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("673121")

        # Continue checkout
        driver.find_element(By.ID, "continue").click()

        # Verify overview page
        wait.until(EC.url_contains("checkout-step-two.html"))

        # Finish order
        driver.find_element(By.ID, "finish").click()

        # Verify order confirmation
        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        assert confirmation.text == "Thank you for your order!"

        print("TEST PASSED: Checkout completed successfully")

    except Exception as error:
        print("TEST FAILED:", error)
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_checkout()
