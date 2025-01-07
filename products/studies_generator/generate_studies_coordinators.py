import random
from config.product_config import ProductsConfig, ProductType
from config.user_config import UserConfig, UserRoleType

class StudiesCoordinator:
    def __init__(self, coordinator_id, study_id):
        self.CoordinatorID = coordinator_id
        self.StudyID = study_id

def generate_studies_coordinators():
    studies_coordinators = []
    studies_ranges = ProductsConfig.get_products_ranges()[ProductType.STUDIES]
    coordinator_range = UserConfig.get_role_ranges()[UserRoleType.COORDINATOR]

    for study_id in range(studies_ranges[0], studies_ranges[1] + 1):
        coordinator_ids = random.sample(range(coordinator_range[0], coordinator_range[1] + 1), random.randint(1, 3))
        for coordinator_id in coordinator_ids:
            studies_coordinators.append(vars(StudiesCoordinator(coordinator_id, study_id)))

    return studies_coordinators