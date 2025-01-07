import random

from config.product_config import ProductsConfig, ProductType
from config.user_config import UserConfig
from orders.generate_orders import OrderDetails


class StudiesParticipants:
    def __init__(self, studies_id, participant_id):
        self.StudyID = studies_id
        self.ParticipantID = participant_id


def generate_participants_studies_and_orders():
    studies_participants = []
    order_details = []
    existing_pairs = set()
    participants_studies_ranges = UserConfig.get_product_ranges()[ProductType.STUDIES]
    studies_range = ProductsConfig.get_products_ranges()[ProductType.STUDIES]

    for participants_studies_range in participants_studies_ranges:
        for i in range(participants_studies_range[0], participants_studies_range[1] + 1):
            studies_id = random.randint(studies_range[0], studies_range[1])

            if (studies_id, i) in existing_pairs:
                continue

            studies_participants.append(vars(StudiesParticipants(studies_id, i)))


            existing_pairs.add((studies_id, i))

            price = random.randint(50, 500)
            order_id = i - UserConfig.get_total_orders()
            order_details.append(vars(OrderDetails(order_id, studies_id, price)))

    return studies_participants, order_details
