from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode for efficiency
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Navigate to the login page
    driver.get("https://poe.com/login")
    
    # Click the "Use phone" button
    use_phone_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Use phone')]")
    use_phone_button.click()
    
    # Wait for the phone number input to be visible
    time.sleep(2)  # Adjust the sleep time as necessary for your network speed
    
    # Enter the phone number
    phone_input = driver.find_element(By.XPATH, "//input[@placeholder='Phone number']")
    phone_input.send_keys("18338191679")
    
    # Click the "Go" button
    go_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Go')]")
    go_button.click()
    
    # Additional steps can be added here if needed, such as handling the next page or verifying login success

finally:
    # Close the WebDriver
    driver.quit()
