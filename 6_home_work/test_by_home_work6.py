def test_current_url(driver):
    print(driver.current_url)
    assert "http://localhost/" == driver.current_url
