from dict_theaters import *
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re,requests
from theaters_search.theaters.class_theaters import Theater

class CineCol(Theater):
    def __init__(self):
        super().__init__('cine_col')

    def get_films(self, city):
        url = theaters_url[self.name][0].format(city=city)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        all_films = soup.select(".movie-item")
        
        if city not in self.films:
            self.films[city] = {}
            self.locations[city] = {}

        for film in all_films:
            us_name = film.select_one('.movie-item__title').get_text(strip=True)
            name = film.select_one('.movie-item__meta').get_text(strip=True)
            #---------------------------------------------------------------------------
            #   fixing name so that can the function time can be searched by name
            #--------------------------------------------------------------------------    
            name = re.sub(r"Título en español:\s*(.+)",r'\1', name)
            name= self.normalize_name(name)
            url_name = self.url_name(us_name)
            self.films[city][name] = url_name
    

    def search_showtimes_film(self,films, film,city):
        url_names = films[film]#.url_name
        url_name = self.verify(url_names,city)

        if not url_name:
            return f'No hay funciones de {film} en {self.name}'
        
        url = theaters_url[self.name][1].format(city=city,url_name=url_name)
        #---------------------------------------------------------------------
        #       since the show times and locations load with js file, 
        #   it has to wait to the content to load so i had to use selenium 
        #---------------------------------------------------------------------
        driver = self.get_driver(url)

        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.CLASS_NAME,'show-times-collapse__title')))
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            malls = soup.select('.show-times-collapse__title')
            times = soup.select('.show-times-group__times')
            if city not in self.locations[city]:
                    self.locations[city][film] =  {}

            for idx,mall in enumerate(malls):
                mall = mall.get_text(strip=True)
                time = re.sub(r'(AM|PM)(?!\s)', r'\1 ', times[idx].get_text(strip=True))
                print(f'{mall}\nHorarios: {time}')
                self.locations[city][film][mall] = time

        finally:
            driver.quit()



#-------------------------------------------------------------------------------------------------------------
#                                     Filter of the showtimes 
#   <div class="column is-12">
#   date-filter :is-loading="isLoading" @change="dateChanged" first-function-date="2025-09-10"></date-filter>
#   </div>
#
#-------------------------------------------------------------------------------------------------------------
