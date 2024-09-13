import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_poe_login(driver):
    try:
        driver.get("https://poe.com/login")
        
        use_phone_button = driver.find_element(By.CLASS_NAME, "Button_flat__dcKQ1")
        use_phone_button.click()
        
        time.sleep(2)
        
        phone_input = driver.find_element(By.CLASS_NAME, "textInput_input__9YpqY")
        phone_input.send_keys("18312210562")
        
        go_button = driver.find_element(By.CLASS_NAME, "Button_primary__6UIn0")
        go_button.click()
        
        # Add assertions here to verify the login process
        assert "Poe" in driver.title, "Login page title is incorrect"
        
    except Exception as e:
        pytest.fail(f"Test failed with exception: {str(e)}")
