from theaters_search.libraries import *
from theaters_search.dict_theaters import cine_colombia_ids, cine_colombia_siteids
    
class CineCol(Theater):
    def __init__(self):
        super().__init__('cine_col')

    def get_films(self, city):
        #----------------------------------------------------------------------------------------
        #                  Add siteIds from the city to request data 
        #----------------------------------------------------------------------------------------
        url = 'https://digital-api.cinecolombia.com/ocapi/v1/film-screening-dates?'
        url = self.add_ids_to_url(city,url)
        token = self.get_token()
        resp = requests.get(url,headers={"Authorization": token})
        data = resp.json()
        data = data['filmScreeningDates'][0]['filmScreenings']
        #----------------------------------------------------------------------------------------
        #                   Get films screenings from today
        #----------------------------------------------------------------------------------------
        films_ids = {} 
        for film_id in data:
            # films_ids.append(film_id['filmId'])
            films_ids[film_id['filmId']] = ''

        return token,films_ids 

    def get_film_names(self,films,token,city):
        url = 'https://digital-api.cinecolombia.com/ocapi/v1/films/'
        if city not in self.films:
            self.films[city] = {}
            self.locations[city] = {}
        
        for film in films:
            new_url = url + f'{film}'
            resp = requests.get(new_url,headers={"Authorization": token})
            data = resp.json()
            name = data['film']['title']['translations'][0]['text']
            # name = data['film']['title']['text'] english name
            self.films[city][name] = film 


    def search_showtimes_film(self,film_name,film, city,token):
        # url_names = film
        # url_name = self.verify(url_names,city)
        # if not url_name:
        #     return f'No hay funciones de {film_name} en {self.name}'       

        url = 'https://digital-api.cinecolombia.com/ocapi/v1/showtimes/by-business-date/first?'
        url += f'filmIds={self.films[city][film_name]}&'  
        url = self.add_ids_to_url(city,url)
        resp = requests.get(url,headers={"Authorization": token})
        data = resp.json()
        
        for show in data['showtimes']:
            time = show['schedule']['startsAt']
            time = datetime.fromisoformat(time).strftime("%H:%M")
            mall = show['siteId']
            mall = cine_colombia_siteids[mall]

            if film_name not in self.locations[city]:
                    self.locations[city][film_name] = {}

            if mall not in self.locations[city][film_name]:
                self.locations[city][film_name][mall] = []     
            
            self.locations[city][film_name][mall].append(time)

    def add_ids_to_url(self,city,url):
        ids = cine_colombia_ids[city]
        i = 0
        while i < len(ids) - 1:
            url += f'siteIds={ids[i]}&'
            i += 1
        url += f'siteIds={ids[i]}'
        return url

    def get_token(self):
        captured = {}
        all_requests = []

        with sync_playwright() as p:
            browser = p.firefox.launch(headless=True)
            page = browser.new_page()

            def handle_request(request):
                all_requests.append(request.url)
                auth = request.headers.get("authorization")
                if auth:
                    if "digital-api" in request.url:
                        captured["token"] = auth

            page.on("request", handle_request)

            page.goto("https://www.cinecolombia.com/", wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(10000)

            browser.close()

        return captured.get("token")

