from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from abc import ABC, abstractmethod
import unicodedata,re
from theaters_search.libraries import *

class Theater(ABC):
    def __init__(self, name):
        self.name = name
        self.films = {}
        self.locations = {}

    #-------------------------------------------------------
    #          Get only the films on theaters 
    #-------------------------------------------------------
    @abstractmethod
    def get_films(self, city):
        pass

    #-------------------------------------------------------
    #           Get locations and showtimes 
    #-------------------------------------------------------
    @abstractmethod
    def search_showtimes_film(self, films,film, city):
        pass

    def verify(self,url_names,city):
        #----------------------------------------------
        #       url_names has to be a list
        #----------------------------------------------
        for url_name in url_names:
            if url_name in self.films[city].values():
                return url_name
            
        return False
    
    def get_driver(self,url,class_to_search):
        firefox_options= Options()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(url)
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.CLASS_NAME,class_to_search)))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        
        return soup
    
    def normalize_name(self,name):
        name = unicodedata.normalize("NFD", name)
        name = "".join(ch for ch in name if unicodedata.category(ch) != "Mn")
        name = name.replace("‘", "").replace("’", "").replace("“", '').replace("”", '').replace('–','-')
        
        return name
    
    def url_name(self,name):
        return re.sub(r'[:\s-]+', '-', name)
