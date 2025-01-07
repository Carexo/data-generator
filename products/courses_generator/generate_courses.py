import random
from config.product_config import ProductType, ProductsConfig

course_names = [
    "Wprowadzenie do Pythona",
    "Zaawansowane uczenie maszynowe",
    "Podstawy nauki o danych",
    "Tworzenie stron internetowych z Django",
    "Głębokie uczenie z TensorFlow",
    "Przetwarzanie języka naturalnego",
    "Systemy zarządzania bazami danych",
    "Przetwarzanie w chmurze z AWS",
    "Podstawy cyberbezpieczeństwa",
    "Zasady inżynierii oprogramowania",
    "Podstawy fotografii",
    "Wprowadzenie do jogi",
    "Techniki zarządzania czasem",
    "Podstawy planowania finansowego",
    "Warsztaty pisania kreatywnego",
    "Podstawy projektowania graficznego",
    "Wprowadzenie do teorii muzyki",
    "Podstawy ogrodnictwa",
    "Techniki medytacji i uważności",
    "Planowanie podróży"
]

course_descriptions = [
    "Naucz się podstaw programowania w Pythonie.",
    "Poznaj zaawansowane techniki uczenia maszynowego.",
    "Zrozum podstawy nauki o danych.",
    "Twórz aplikacje internetowe za pomocą frameworka Django.",
    "Zanurz się w głębokie uczenie z TensorFlow.",
    "Poznaj techniki przetwarzania języka naturalnego.",
    "Zarządzaj i projektuj systemy baz danych.",
    "Rozpocznij pracę z przetwarzaniem w chmurze na AWS.",
    "Poznaj podstawy cyberbezpieczeństwa.",
    "Zrozum zasady inżynierii oprogramowania.",
    "Poznaj podstawy fotografii.",
    "Wprowadzenie do praktyki jogi.",
    "Naucz się technik zarządzania czasem.",
    "Poznaj podstawy planowania finansowego.",
    "Rozwijaj swoje umiejętności pisania kreatywnego.",
    "Poznaj podstawy projektowania graficznego.",
    "Wprowadzenie do teorii muzyki.",
    "Poznaj podstawy ogrodnictwa.",
    "Naucz się technik medytacji i uważności.",
    "Poznaj wskazówki dotyczące planowania podróży."
]

class Courses:
    def __init__(self, course_id, name, description, limit_places):
        self.CourseID = course_id
        self.Name = name
        self.Description = description
        self.LimitPlaces = limit_places

def generate_courses():
    courses = []
    course_range = ProductsConfig.get_products_ranges()[ProductType.COURSE]

    for i in range(course_range[0], course_range[1] + 1):
        name = random.choice(course_names)
        description = random.choice(course_descriptions)
        limit_places = random.randint(20, 60)
        courses.append(vars(Courses(i, name, description, limit_places)))


    return courses