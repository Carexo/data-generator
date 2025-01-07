import random

from config.product_config import ProductType, ProductsConfig
from config.user_config import UserConfig
from orders.generate_orders import OrderDetails


class MeetingsSchedules:
    def __init__(self, meeting_id, participant_id, presence):
        self.MeetingID = meeting_id
        self.ParticipantID = participant_id
        self.Presence = presence

def generate_meetings_schedules_and_orders():
    meetings_schedules = []
    order_details = []
    existing_pairs = set()

    participants_meetings_ranges = UserConfig.get_product_ranges()[ProductType.MEETING]
    meeting_range = ProductsConfig.get_products_ranges()[ProductType.MEETING]

    for participants_meetings_range in participants_meetings_ranges:
        for i in range(participants_meetings_range[0], participants_meetings_range[1] + 1):
            meeting_id = random.randint(meeting_range[0], meeting_range[1])
            presence = 1 if random.random() < 0.8 else 0

            if (meeting_id, i) in existing_pairs:
                continue

            existing_pairs.add((meeting_id, i))
            meetings_schedules.append(vars(MeetingsSchedules(meeting_id, i, presence)))

            price = random.randint(50, 500)
            order_id = i - UserConfig.get_total_orders()
            order_details.append(vars(OrderDetails(order_id, meeting_id, price)))

    return meetings_schedules, order_details