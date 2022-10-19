import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome = Service(
    executable_path='/Users/matheus/Downloads/chromedriver', log_path='NUL')

options = Options()
options.add_argument('window-size=400,800')
options.add_experimental_option("detach", True)

navegador = webdriver.Chrome(service=chrome, options=options)

navegador.get(
    'https://jastrack.jas.com/Login/Login.aspx?ReturnUrl=%2fDefault.aspx')
