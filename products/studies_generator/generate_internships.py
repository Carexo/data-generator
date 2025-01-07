import random
from datetime import datetime, timedelta

from config.product_config import ProductsConfig, ProductType
from config.user_config import UserConfig, UserRoleType
from utils.random_data import random_date


class InternshipDetails:
    def __init__(self, studies_id, participant_id, start_date, end_date):
        self.StudyID = studies_id
        self.ParticipantID = participant_id
        self.StartDate = start_date
        self.EndDate = end_date



def generate_internships():
    internships = []
    studies_ranges = ProductsConfig.get_products_ranges()[ProductType.STUDIES]
    participants_range = UserConfig.get_role_ranges()[UserRoleType.PARTICIPANT]

    for studies_id in range(studies_ranges[0], studies_ranges[1] + 1):
        participant_ids = random.sample(range(participants_range[0], participants_range[1] + 1), random.randint(1, 3))
        for participant_id in participant_ids:
            start_date = random_date(2020, 2024).strftime("%Y-%m-%d %H:%M:%S")
            if random.random() < 0.8:
                end_date = (datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S") + timedelta(days=14)).strftime("%Y-%m-%d %H:%M:%S")
            else:
                end_date = (datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S") + timedelta(days=random.randint(1, 13))).strftime(
                    "%Y-%m-%d %H:%M:%S")
            internships.append(vars(InternshipDetails(studies_id, participant_id, start_date, end_date)))

    return internships
