from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep

# chr_options = ChromeOptions()
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chr_options)
driver = webdriver.Chrome()
driver.get("https://www.google.com")
sleep(2)
