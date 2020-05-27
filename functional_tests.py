from selenium import webdriver
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://localhost:3000')
try:
    assert 'To-Do' in browser.title, "Browser title was " + browser.title
finally:
    browser.close()
    browser.quit()
