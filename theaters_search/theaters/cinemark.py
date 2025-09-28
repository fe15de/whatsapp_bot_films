from dict_theaters import *
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import requests,json
from  theaters_search.theaters.class_theaters import Theater

class Cinemark(Theater):
    def __init__(self):
        super().__init__('cinemark')

    def get_films(self, city):

        url = theaters_url[self.name][0].format(city=city)
        driver = self.get_driver(url)
        #-------------------------------------------------------
        #               Wait javascript to load
        #-------------------------------------------------------
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.CLASS_NAME,'billboard-movies')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        section = soup.find("section", class_="billboard-movies")
        cards = section.find_all("div", class_="grid-movie__card")
        
        if city not in self.films:
            self.films[city] = {}
            self.locations[city] = {}

        for card in cards:
            name = card.find("h3", class_="info-movie__title-movie")
            name= self.normalize_name(name.text.strip())
            url_name = self.url_name(name)
            self.films[city][name] = url_name
    

    def search_showtimes_film(self, films, film, city):
        url_names = films[film]#.url_name
        url_name = self.verify(url_names,city)
        
        if not url_name:
            return False
        url = theaters_url[self.name][1].format(city=city,url_name=url_name)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        #--------------------------------------------------------------------------
        #                   Get id of the film to get showtimes
        # -------------------------------------------------------------------------
        script = soup.find("script", {"id": "__NEXT_DATA__"})
        data = json.loads(script.string)
        movie = data["props"]["pageProps"]["movie"]
        film_id = movie["CorporateFilmId"]
        today_date = date.today().strftime("%Y-%m-%d")
        url = f"https://api.cinemark-core.com/vista/country/co/city/{city}/movie/{film_id}?date={today_date}&companyId=5db771be04daec00076df3f5&midnightSessionStart=22&midnightSessionEnd=02"
        headers = {
            "connectapitoken": "a"
        }
        resp = requests.get(url,headers=headers)
        data = resp.json()

        for theater in data["Theater"]:
            msg = '' 
            for fmt in theater["Format"]:
                for session in fmt["Sessions"]:
                    if session["IsVisible"]:
                        msg +=f"{session['Showtime']} {session['SeatsAvailable']} asientos" 
            if film not in self.locations[city]:
                    self.locations[city][film] =  {}
            
            self.locations[city][film][theater['Name']] = msg