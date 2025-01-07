from address.generate_address import generate_address
from config.address_config import AddressConfig

from data_generator import generate_inserts

tables = {
    "Countries": ["CountryID", "CountryName"],
    "Cities": ["CityID", "CountryID", "CityName"],
    "Addresses": ["AddressID", "CityID", "Address", "PostalCode"]
}

sample_data = {
    "Countries": [
    {"CountryID": 1, "CountryName": "Polska"},
    {"CountryID": 2, "CountryName": "Niemcy"},
    {"CountryID": 3, "CountryName": "Francja"},
    {"CountryID": 4, "CountryName": "Włochy"},
    {"CountryID": 5, "CountryName": "Hiszpania"},
],
    "Cities": [
    {"CityID": 1, "CountryID": 1, "CityName": "Warszawa"},
    {"CityID": 2, "CountryID": 1, "CityName": "Kraków"},
    {"CityID": 3, "CountryID": 1, "CityName": "Łódź"},
    {"CityID": 4, "CountryID": 1, "CityName": "Wrocław"},
    {"CityID": 5, "CountryID": 1, "CityName": "Poznań"},
    {"CityID": 6, "CountryID": 1, "CityName": "Gdańsk"},
    {"CityID": 7, "CountryID": 1, "CityName": "Szczecin"},
    {"CityID": 8, "CountryID": 1, "CityName": "Bydgoszcz"},
    {"CityID": 9, "CountryID": 1, "CityName": "Lublin"},
    {"CityID": 10, "CountryID": 1, "CityName": "Katowice"},
    {"CityID": 11, "CountryID": 2, "CityName": "Berlin"},
    {"CityID": 12, "CountryID": 2, "CityName": "Hamburg"},
    {"CityID": 13, "CountryID": 2, "CityName": "Monachium"},
    {"CityID": 14, "CountryID": 2, "CityName": "Kolonia"},
    {"CityID": 15, "CountryID": 2, "CityName": "Frankfurt"},
    {"CityID": 16, "CountryID": 2, "CityName": "Stuttgart"},
    {"CityID": 17, "CountryID": 2, "CityName": "Düsseldorf"},
    {"CityID": 18, "CountryID": 2, "CityName": "Dortmund"},
    {"CityID": 19, "CountryID": 2, "CityName": "Essen"},
    {"CityID": 20, "CountryID": 2, "CityName": "Leipzig"},
    {"CityID": 21, "CountryID": 3, "CityName": "Paryż"},
    {"CityID": 22, "CountryID": 3, "CityName": "Marsylia"},
    {"CityID": 23, "CountryID": 3, "CityName": "Lyon"},
    {"CityID": 24, "CountryID": 3, "CityName": "Tuluza"},
    {"CityID": 25, "CountryID": 3, "CityName": "Nicea"},
    {"CityID": 26, "CountryID": 3, "CityName": "Nantes"},
    {"CityID": 27, "CountryID": 3, "CityName": "Strasbourg"},
    {"CityID": 28, "CountryID": 3, "CityName": "Montpellier"},
    {"CityID": 29, "CountryID": 3, "CityName": "Bordeaux"},
    {"CityID": 30, "CountryID": 3, "CityName": "Lille"},
    {"CityID": 31, "CountryID": 4, "CityName": "Rzym"},
    {"CityID": 32, "CountryID": 4, "CityName": "Mediolan"},
    {"CityID": 33, "CountryID": 4, "CityName": "Neapol"},
    {"CityID": 34, "CountryID": 4, "CityName": "Turyn"},
    {"CityID": 35, "CountryID": 4, "CityName": "Palermo"},
    {"CityID": 36, "CountryID": 4, "CityName": "Genua"},
    {"CityID": 37, "CountryID": 4, "CityName": "Bologna"},
    {"CityID": 38, "CountryID": 4, "CityName": "Florencja"},
    {"CityID": 39, "CountryID": 4, "CityName": "Bari"},
    {"CityID": 40, "CountryID": 4, "CityName": "Catania"},
    {"CityID": 41, "CountryID": 5, "CityName": "Madryt"},
    {"CityID": 42, "CountryID": 5, "CityName": "Barcelona"},
    {"CityID": 43, "CountryID": 5, "CityName": "Walencja"},
    {"CityID": 44, "CountryID": 5, "CityName": "Sewilla"},
    {"CityID": 45, "CountryID": 5, "CityName": "Zaragoza"},
    {"CityID": 46, "CountryID": 5, "CityName": "Málaga"},
    {"CityID": 47, "CountryID": 5, "CityName": "Murcia"},
    {"CityID": 48, "CountryID": 5, "CityName": "Palma"},
    {"CityID": 49, "CountryID": 5, "CityName": "Las Palmas"},
    {"CityID": 50, "CountryID": 5, "CityName": "Bilbao"}
],
    "Addresses": generate_address(AddressConfig.get_total_addresses())}

generate_inserts(tables, sample_data, "addresses_insert_data.sql")