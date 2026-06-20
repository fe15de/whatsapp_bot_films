from theaters_search.libraries import *
from theaters_search.dict_theaters import cities_id_royal
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RoyalFilms(Theater):
    def __init__(self):
        super().__init__('royal_films')
        self.city_id = ''

    def get_films(self, city):
        self.city_id = cities_id_royal[city]
        url = f'https://cinemasroyalfilms.com/api/billboard/city/{self.city_id}'
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        resp = requests.get(url,verify=False,headers=headers)
        data = resp.json()
        data = data['data']

        if not city in self.films:
            self.films[city] = {}
        
        for film in data:
            name= self.normalize_name(film['pelicula']['pelicula_nombre_formato'])
            self.films[city][name] = str(film['pelicula']['pelicula_id'])  

    def search_showtimes_film(self, film_name, film, city):
        url_names = film.url_name
        # url_names = film
        film_id = self.verify(url_names,city)
        
        if not film_id:
            return f'No hay funciones de {film_name} en {self.name}'
        
        url = f'https://cinemasroyalfilms.com/api/movies/functions/{film_id}/city/{self.city_id}'
        if city not in self.locations:
                    self.locations[city] =  {}
        resp = requests.get(url,verify=False)
        data = resp.json()
        data= data['data']

        for show in data: 
            mall = show['multicine']['multicine_nombre']
            time = show['funcion_hora_inicio']
            time = datetime.fromisoformat(time.replace("Z", "+00:00"))
            time = time.strftime("%H:%M")
            if film_name not in self.locations[city]:
                    self.locations[city][film_name] = {}

            if mall not in self.locations[city][film_name]:
                self.locations[city][film_name][mall] = []     
            
            self.locations[city][film_name][mall].append(time)
            
