import random
from config.study_config import StudyConfig


class Subject:
    def __init__(self, subject_id, name, description, duration):
        self.SubjectID = subject_id
        self.Name = name
        self.Description = description
        self.Duration = duration

subject_names = [
    "Podstawy Matematyki",
    "Wprowadzenie do Fizyki",
    "Chemia Organiczna",
    "Biologia Molekularna",
    "Historia Starożytna",
    "Geografia Fizyczna",
    "Literatura Polska",
    "Filozofia Współczesna",
    "Psychologia Rozwojowa",
    "Socjologia Kultury",
    "Ekonomia Mikro",
    "Zarządzanie Projektami",
    "Prawo Cywilne",
    "Inżynieria Oprogramowania",
    "Sztuczna Inteligencja",
    "Analiza Danych",
    "Cyberbezpieczeństwo",
    "Robotyka",
    "Marketing Cyfrowy",
    "Finanse i Rachunkowość",
    "Podstawy Statystyki",
    "Wprowadzenie do Astronomii",
    "Chemia Fizyczna",
    "Biologia Komórkowa",
    "Historia Średniowiecza",
    "Geografia Społeczna",
    "Literatura Światowa",
    "Filozofia Antyczna",
    "Psychologia Kliniczna",
    "Socjologia Rodziny",
    "Ekonomia Makro",
    "Zarządzanie Zasobami Ludzkimi",
    "Prawo Karne",
    "Inżynieria Systemów",
    "Uczenie Maszynowe",
    "Analiza Finansowa",
    "Bezpieczeństwo Sieci",
    "Automatyka",
    "Reklama Cyfrowa",
    "Rachunkowość Zarządcza"
]

subject_descriptions = [
    "Podstawowe zagadnienia matematyczne.",
    "Wprowadzenie do zasad fizyki.",
    "Podstawy chemii organicznej.",
    "Biologia na poziomie molekularnym.",
    "Historia starożytnych cywilizacji.",
    "Geografia fizyczna i jej zjawiska.",
    "Analiza literatury polskiej.",
    "Filozofia współczesna i jej nurty.",
    "Psychologia rozwoju człowieka.",
    "Socjologia kultury i społeczeństwa.",
    "Podstawy ekonomii mikro.",
    "Techniki zarządzania projektami.",
    "Podstawy prawa cywilnego.",
    "Zasady inżynierii oprogramowania.",
    "Wprowadzenie do sztucznej inteligencji.",
    "Techniki analizy danych.",
    "Podstawy cyberbezpieczeństwa.",
    "Robotyka i automatyka.",
    "Marketing cyfrowy i jego narzędzia.",
    "Podstawy finansów i rachunkowości.",
    "Podstawy statystyki i analizy danych.",
    "Wprowadzenie do astronomii i kosmologii.",
    "Podstawy chemii fizycznej.",
    "Biologia komórkowa i genetyka.",
    "Historia średniowiecznych społeczeństw.",
    "Geografia społeczna i urbanistyka.",
    "Analiza literatury światowej.",
    "Filozofia antyczna i jej myśliciele.",
    "Psychologia kliniczna i terapia.",
    "Socjologia rodziny i relacji społecznych.",
    "Podstawy ekonomii makro.",
    "Zarządzanie zasobami ludzkimi.",
    "Podstawy prawa karnego.",
    "Inżynieria systemów i sieci.",
    "Uczenie maszynowe i sztuczna inteligencja.",
    "Analiza finansowa i inwestycje.",
    "Bezpieczeństwo sieci i systemów.",
    "Automatyka i sterowanie.",
    "Reklama cyfrowa i media społecznościowe.",
    "Rachunkowość zarządcza i kontroling."
]

def generate_subjects():
    subjects = []

    for i in range(1, StudyConfig.get_total_subjects() + 1):
        name = random.choice(subject_names)
        description = random.choice(subject_descriptions)
        duration = random.randint(10, 60)
        subjects.append(vars(Subject(i, name, description, duration)))

    return subjects