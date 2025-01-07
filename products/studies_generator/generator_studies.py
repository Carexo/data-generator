import random

from config.product_config import ProductType, ProductsConfig

studies_names = [
    "Inżynieria Oprogramowania",
    "Zarządzanie Projektami",
    "Sztuczna Inteligencja",
    "Analiza Danych",
    "Cyberbezpieczeństwo",
    "Inżynieria Biomedyczna",
    "Robotyka",
    "Zarządzanie Zasobami Ludzkimi",
    "Marketing Cyfrowy",
    "Finanse i Rachunkowość",
    "Prawo",
    "Psychologia",
    "Socjologia",
    "Filozofia",
    "Biotechnologia",
    "Fizyka",
    "Chemia",
    "Matematyka",
    "Geografia",
    "Historia"
]

studies_descriptions = [
    "Studia z zakresu inżynierii oprogramowania.",
    "Nauka zarządzania projektami.",
    "Poznaj tajniki sztucznej inteligencji.",
    "Analiza danych i big data.",
    "Podstawy cyberbezpieczeństwa.",
    "Inżynieria biomedyczna i technologie medyczne.",
    "Robotyka i automatyka.",
    "Zarządzanie zasobami ludzkimi.",
    "Marketing cyfrowy i media społecznościowe.",
    "Finanse i rachunkowość.",
    "Studia prawnicze.",
    "Psychologia i badania nad zachowaniem.",
    "Socjologia i badania społeczne.",
    "Filozofia i myślenie krytyczne.",
    "Biotechnologia i inżynieria genetyczna.",
    "Fizyka teoretyczna i eksperymentalna.",
    "Chemia organiczna i nieorganiczna.",
    "Matematyka stosowana i teoretyczna.",
    "Geografia fizyczna i społeczna.",
    "Historia i badania historyczne."
]

class Studies:
    def __init__(self, studies_id, name, description, limit_places, start_year):
        self.StudyID = studies_id
        self.Name = name
        self.Description = description
        self.LimitPlaces = limit_places
        self.StartYear = start_year

def generate_studies():
    studies = []
    studies_range = ProductsConfig.get_products_ranges()[ProductType.STUDIES]
    for i in range(studies_range[0], studies_range[1] + 1):
        name = random.choice(studies_names)
        description = random.choice(studies_descriptions)
        limit_places = random.randint(10, 100)
        start_year = random.choice([2020, 2021, 2022])
        studies.append(vars(Studies(i, name, description, limit_places, start_year)))

    return studies