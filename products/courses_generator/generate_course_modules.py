import random

from config.course_config import CourseConfig
from config.product_config import ProductType, ProductsConfig


class CourseModule:
    def __init__(self, module_id, name, description, course_id, module_type_id):
        self.ModuleID = module_id
        self.Name = name
        self.Description = description
        self.CourseID = course_id
        self.ModuleTypeID = module_type_id

module_names = [
    "Podstawy programowania",
    "Zaawansowane algorytmy",
    "Wprowadzenie do baz danych",
    "Projektowanie stron internetowych",
    "Analiza danych",
    "Uczenie maszynowe",
    "Podstawy fotografii",
    "Techniki medytacji",
    "Planowanie finansowe",
    "Podstawy ogrodnictwa",
    "Historia sztuki",
    "Podstawy marketingu",
    "Wprowadzenie do psychologii",
    "Podstawy zarządzania",
    "Wprowadzenie do socjologii",
    "Podstawy ekonomii",
    "Podstawy geografii",
    "Wprowadzenie do filozofii",
    "Podstawy chemii",
    "Podstawy fizyki"
]

module_descriptions = [
    "Naucz się podstaw programowania.",
    "Poznaj zaawansowane algorytmy.",
    "Wprowadzenie do baz danych.",
    "Projektowanie stron internetowych.",
    "Analiza danych.",
    "Uczenie maszynowe.",
    "Poznaj podstawy fotografii.",
    "Techniki medytacji.",
    "Planowanie finansowe.",
    "Podstawy ogrodnictwa.",
    "Historia sztuki.",
    "Podstawy marketingu.",
    "Wprowadzenie do psychologii.",
    "Podstawy zarządzania.",
    "Wprowadzenie do socjologii.",
    "Podstawy ekonomii.",
    "Podstawy geografii.",
    "Wprowadzenie do filozofii.",
    "Podstawy chemii.",
    "Podstawy fizyki."
]

def generate_course_modules():
    course_modules = []
    modules_ranges = CourseConfig.get_module_ranges()
    course_range = ProductsConfig.get_products_ranges()[ProductType.COURSE]

    for module_type, range_value in modules_ranges.items():
        j = course_range[0]
        for i in range(range_value[0], range_value[1] + 1):
            course_id = j
            j += 1
            if j > course_range[1]:
                j = course_range[0]
            module_id = i
            name = random.choice(module_names)
            description = random.choice(module_descriptions)

            course_modules.append(vars(CourseModule(module_id, name, description, course_id, module_type.value)))

    return course_modules