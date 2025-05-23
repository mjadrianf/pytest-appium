from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search(driver):
    driver.get("https://www.google.com")

    try:
        accept_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "L2AGLb"))
        )
        accept_btn.click()
    except:
        pass

    # Ahora esperamos el campo de búsqueda
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("pytest appium")
