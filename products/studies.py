from data_generator import generate_inserts
from products.studies_generator.generate_internships import generate_internships
from products.studies_generator.generate_studies_coordinators import generate_studies_coordinators
from products.studies_generator.generate_syllabuses import generate_syllabuses
from products.studies_generator.generator_studies import generate_studies
from products.studies_generator.generator_subjects import generate_subjects

tables = {
    "Studies": ["StudyID", "Name", "Description", "LimitPlaces", "StartYear"],
    "StudiesCoordinators": ["StudyID", "CoordinatorID"],
    "Subjects": ["SubjectID", "Name", "Description", "Duration"],
    "Syllabuses": ["SubjectID", "StudyID", "Semester"],
    "InternshipsDetails": ["StudyID", "ParticipantID", "StartDate", "EndDate"],
}


sample_data = {
    "Studies": generate_studies(),
    "StudiesCoordinators": generate_studies_coordinators(),
    "Subjects": generate_subjects(),
    "Syllabuses": generate_syllabuses(),
    "InternshipsDetails": generate_internships(),
}

generate_inserts(tables, sample_data, "studies_data.sql")