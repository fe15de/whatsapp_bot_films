from dict_theaters import *
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from theaters_search.theaters.class_theaters import Theater

class Cinepolis(Theater):
    def __init__(self):
        super().__init__('cinepolis')

    def get_films(self, city):
        url = theaters_url[self.name][0].format(city=city)
        driver = self.get_driver(url)
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.CLASS_NAME,'listaCarteleraHorario')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        if city not in self.films:
            self.films[city] = {}
            self.locations[city] = {}

        for complejo in soup.find_all("div", class_="divComplejo"):
            mall = complejo.find("h2").get_text(strip=True).replace(" ?", "")
            
            for film in complejo.find_all("article", class_="tituloPelicula"):
                name =film.find("a", class_="datalayer-movie").get_text(strip=True)
                name= self.normalize_name(name)
                url_name = self.url_name(name)
                self.films[city][name] = url_name

                section = film.find('div',class_='descripcion')
                horarios = [
                    t.get_text(strip=True)
                    for t in section.find_all("a", class_="ng-binding")
                ]
                #print(mall,name,horarios)
                if name not in self.locations[city]:
                    self.locations[city][name] =  {}
                
                self.locations[city][name][mall] = horarios[1:]

        

    def search_showtimes_film(self, films, film, city):
        if film in self.films[city]:
            print(self.locations[city][film])