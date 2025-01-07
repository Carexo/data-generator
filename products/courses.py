from config.course_config import ModuleType
from data_generator import generate_inserts
from products.courses_generator.genearte_courses_coordinators import generate_courses_coordinators
from products.courses_generator.generate_course_modules import generate_course_modules
from products.courses_generator.generate_courses import generate_courses

tables = {
    "ModuleType": ["ModuleTypeID", "Type"],
    "Courses": ["CourseID", "Name", "Description", "LimitPlaces"],
    "CourseModule": ["ModuleID", "Name", "Description", "CourseID", "ModuleTypeID"],
    "CoursesCoordinators": ["CoursesID", "CourseCoordinatorID"],
}

sample_data = {
   "ModuleType": [
         {"ModuleTypeID": ModuleType.ONLINE_SYNC.value, "Type": "online-synchroniczny"},
         {"ModuleTypeID": ModuleType.ONLINE_ASYNC.value, "Type": "online-asynchroniczny"},
         {"ModuleTypeID": ModuleType.ON_SITE.value, "Type": "stacjonarny"},
         {"ModuleTypeID": ModuleType.HYBRID.value, "Type": "hybrydowy"},
   ],
    "Courses": generate_courses(),
    "CourseModule": generate_course_modules(),
    "CoursesCoordinators": generate_courses_coordinators(),
}

generate_inserts(tables, sample_data, "courses_data.sql")
