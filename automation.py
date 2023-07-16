import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Set up the Selenium webdriver (using Chrome in this example)
driver = webdriver.Chrome()  # Update with the actual path to the Chrome driver
driver.maximize_window()

# Navigate to the webpage
driver.get("https://mounikak.in/portfolio/stock/index.html")

# Click on the Login button
login_button = driver.find_element(By.XPATH, "/html/body/header/div[3]/div[1]/span")
login_button.click()
    
# Wait for the login form to appear
wait = WebDriverWait(driver, 60)
login_form = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]")))

# Enter ticker value
wait = WebDriverWait(driver, 60)
ticker_input = driver.find_element(By.ID, "ticker")
ticker_input.send_keys("AAPL")

# Enter range value
wait = WebDriverWait(driver, 60)
range_input = driver.find_element(By.ID, "range")
range_input.send_keys("1")


# Select the From Date as 01.07.2023
from_date = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div/input")
from_date.clear()
from_date.send_keys("01.07.2023")


# Select the To Date as 08.07.2023
to_date = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/input")
to_date.clear()
to_date.send_keys("08.07.2023")

# Submit the form
submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[6]/button")
submit_button.click()

# Dummy Wait for the results to be shown
results_table = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[3]/table/tbody")))
wait = WebDriverWait(driver, 20)

# Close the browser
driver.quit()
