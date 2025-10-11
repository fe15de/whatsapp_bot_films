cities_with_theaters = [
    "Armenia",
    "Barranquilla",
    "Bogotá",
    "Bucaramanga",
    "Buenaventura",
    "Buga",
    "Cali",
    "Cartagena",
    "Cartago",
    "Caucasia",
    "Chía",
    "Cúcuta",
    "Dosquebradas",
    "Envigado",
    "Florencia",
    "Fusagasugá",
    "Girardot",
    "Guajira",
    "Ibagué",
    "Ipiales",
    "Itagüí",
    "Madrid",
    "Manizales",
    "Medellín",
    "Montería",
    "Mosquera",
    "Neiva",
    "Palmira",
    "Pasto",
    "Pereira",
    "Popayán",
    "Santa Marta",
    "Santo Tomás",
    "Sincelejo",
    "Soledad",
    "Tuluá",
    "Tunja",
    "Valledupar",
    "Villavicencio",
    "Yopal",
    "Yumbo"
]


theaters_by_city = {
    "cine_col": [
        "Armenia", "Barranquilla", "Bogotá", "Bucaramanga", "Cali",
        "Cartagena", "Fusagasugá", "Ibagué", "Manizales", "Medellín",
        "Montería", "Pereira", "Popayán", "Villavicencio"
    ],
    "cinemark": [
        "Armenia", "Bogotá", "Bucaramanga", "Cali", "Cúcuta",
        "Florencia", "Ibagué", "Ipiales", "Medellín", "Montería",
        "Neiva", "Palmira", "Pasto", "Pereira", "Santa Marta",
        "Soledad", "Villavicencio", "Yopal"
    ],
    "cinepolis": [
        "Barranquilla", "Bogotá", "Cali", "Manizales", "Valledupar",
        "Chía", "Envigado"
    ],
    "royal_films": [
        "Armenia", "Barranquilla", "Bogotá", "Bucaramanga", "Buenaventura",
        "Buga", "Cali", "Cartagena", "Cartago", "Caucasia", "Cúcuta",
        "Dosquebradas", "Girardot", "Guajira", "Ibagué", "Itagüí",
        "Madrid", "Medellín", "Montería", "Mosquera", "Neiva", "Pasto",
        "Pereira", "Popayán", "Santo Tomás", "Sincelejo", "Tuluá",
        "Tunja", "Valledupar", "Villavicencio", "Yumbo"
    ],
}


theaters_url = {
    'cinemark' : ['https://www.cinemark.com.co/cartelera/{city}','https://www.cinemark.com.co/cartelera/{city}/{url_name}'],
    'cine_col' : ['https://www.cinecolombia.com/{city}/cartelera','https://www.cinecolombia.com/{city}/peliculas/{url_name}'],
    'cinepolis' : ['https://cinepolis.com.co/cartelera/{city}-colombia/',''], # -> In Theaters link gives the showtimes
    'royal_films' : ['https://cinemasroyalfilms.com/cartelera/{city}', ''], # -> In Theaters link gives the link to the showtimes
}
cities_id_royal = {
    "Armenia": "1015",
    "Barranquilla": "6",
    "Bogotá": "1026",
    "Bucaramanga": "1013",
    "Buenaventura": "1023",
    "Buga": "1021",
    "Cali": "1020",
    "Cartagena": "1043",
    "Cartago": "1034",
    "Cúcuta": "1032",
    "Dosquebradas": "1031",
    "Girardot": "1017",
    "Guajira": "1036",
    "Ibagué": "1027",
    "Ibagué": "1027",
    "Itagüí": "1012",
    "Madellín": "1025",
    "Montería": "1035",
    "Mosquera": "1028",
    "Neiva": "1018",
    "Pasto": "1019",
    "Pereira": "1024",
    "Popayán": "1037",
    "Santo Tomás": "1011",
    "Santa Marta": "1010",
    "Villavicencio": "1042",
    "Yumbo": "1043"
}