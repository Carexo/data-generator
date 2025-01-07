import random
from config.product_config import ProductsConfig, ProductType
from config.study_config import StudyConfig


class Syllabus:
    def __init__(self, subject_id, studies_id, semester):
        self.SubjectID = subject_id
        self.StudyID = studies_id
        self.Semester = semester


def generate_syllabuses():
    syllabuses = []
    studies_ranges = ProductsConfig.get_products_ranges()[ProductType.STUDIES]

    for studies_id in range(studies_ranges[0], studies_ranges[1] + 1):
        subject_ids = random.sample(range(1, StudyConfig.get_total_subjects()), random.randint(12,30))

        for subject_id in subject_ids:
            semester = random.randint(1, 10)
            syllabuses.append(vars(Syllabus(subject_id, studies_id, semester)))

    return syllabuses