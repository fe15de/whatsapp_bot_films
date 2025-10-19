from theaters_search.libraries import *
class Cinemark(Theater):
    def __init__(self):
        super().__init__('cinemark')

    def get_films(self, city):
        city_url = self.normalize_name(city)
        url = theaters_url[self.name][0].format(city=city_url)
        soup = self.get_driver(url,'billboard-movies')
        #-------------------------------------------------------
        #               Wait javascript to load
        #-------------------------------------------------------
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
    

    def search_showtimes_film(self, film_name, film, city):
        url_names = film.url_name
        url_name = self.verify(url_names,city)
        
        if not url_name:
            return f'No hay funciones de {film_name} en {self.name}'
        
        url = theaters_url[self.name][1].format(city=city,url_name=url_name)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        #--------------------------------------------------------------------------
        #                   Get id of the film  to get showtimes
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
                        msg +=f"{session['Showtime'][:5]} {session['SeatsAvailable']} asientos\n" 
            if film_name not in self.locations[city]:
                    self.locations[city][film_name] =  {}
            
            self.locations[city][film_name][theater['Name']] = msg