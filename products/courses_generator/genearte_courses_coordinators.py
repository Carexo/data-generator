import random
from config.product_config import ProductType, ProductsConfig
from config.user_config import UserConfig, UserRoleType

class CoursesCoordinators:
    def __init__(self, CoursesID, CourseCoordinatorID):
        self.CoursesID = CoursesID
        self.CourseCoordinatorID = CourseCoordinatorID

def generate_courses_coordinators():
    courses_coordinators = []
    courses_ranges = ProductsConfig.get_products_ranges()[ProductType.COURSE]
    coordinator_range = UserConfig.get_role_ranges()[UserRoleType.COORDINATOR]

    for course_id in range(courses_ranges[0], courses_ranges[1] + 1):
        coordinator_ids = random.sample(range(coordinator_range[0], coordinator_range[1] + 1), random.randint(1, 3))
        for coordinator_id in coordinator_ids:
            courses_coordinators.append(vars(CoursesCoordinators(course_id, coordinator_id)))

    return courses_coordinators
