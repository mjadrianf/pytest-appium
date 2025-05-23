def test_search_booking(driver):
    driver.get("https://www.google.com")

    try:
        accept_btn = driver.find_element("id", "L2AGLb")
        accept_btn.click()
    except:
        pass

    search_box = driver.find_element("name", "q")
    search_box.send_keys("Booking.com")
    search_box.submit()

    assert "booking.com" in driver.page_source.lower()