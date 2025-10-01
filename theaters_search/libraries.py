from theaters_search.dict_theaters import theaters_url
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from theaters_search.theaters.class_theaters import Theater
import re,requests,json
from datetime import date , datetime