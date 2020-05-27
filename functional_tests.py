from selenium import webdriver
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://localhost:8000')
assert 'To-Do' in browser.title._f'browser title was {browser.title}'
