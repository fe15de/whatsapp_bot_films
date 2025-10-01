from theaters_search.libraries import *

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
            url_name = re.sub(r'[^A-Za-z0-9áéíóúÁÉÍÓÚñÑ ]+', '', name)
            url_name = re.sub(r'\s+', '+', url_name)
            
            #url_name = self.url_name(name)
            self.films[city][name] = url_name.upper()

        
    def search_showtimes_film(self, films, film, city):
        url_names = films[film]#.url_name
        url_name = self.verify(url_names,city)

        if not url_name:
            return f'No hay funciones de {film} en {self.name}'
        #----------------------------------------------------------------------------------------
        #                   Use the api instead of scraping (faster)
        #----------------------------------------------------------------------------------------
        today_date = date.today().strftime("%Y-%m-%d")
        url = f'https://funciones.cinecolombia.com/cineco/get-performances-by-params?name={url_name}&date={today_date}&city={city[:3]}'
        resp = requests.get(url)
        data = resp.json()
        if film not in self.locations[city]:
                self.locations[city][film] =  {}
        for location in data:
            mall =  location['Name']
            self.locations[city][film][mall] = []
            showtimes = location['showtimes']
            for type_format in showtimes:
                showtimes = type_format['performances']
                for showtime in showtimes:
                    time = datetime.fromisoformat(showtime['DateTime'])
                    self.locations[city][film][mall].append(time.strftime("%H:%M"))
