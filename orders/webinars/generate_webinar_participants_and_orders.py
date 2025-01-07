import random
from config.product_config import ProductType, ProductsConfig
from config.user_config import UserConfig
from orders.generate_orders import OrderDetails
from utils.random_data import random_date


class WebinarsParticipants:
    def __init__(self, webinar_id, participant_id, available_due):
        self.WebinarID = webinar_id
        self.ParticipantID = participant_id
        self.AvailableDue = available_due



def generate_webinar_participants_and_orders():
    webinars_participants = []
    order_details = []
    existing_pairs = set()
    participants_webinars_ranges = UserConfig.get_product_ranges()[ProductType.WEBINAR]
    webinar_range = ProductsConfig.get_products_ranges()[ProductType.WEBINAR]

    for participants_webinars_range in participants_webinars_ranges:
        for i in range(participants_webinars_range[0], participants_webinars_range[1] + 1):
            webinar_id = random.randint(webinar_range[0], webinar_range[1])
            available_due = random_date(2020, 2024).strftime("%Y-%m-%d %H:%M:%S")

            if (webinar_id, i) in existing_pairs:
                continue

            webinars_participants.append(vars(WebinarsParticipants(webinar_id, i, available_due)))


            existing_pairs.add((webinar_id, i))

            price = random.randint(50, 500)
            order_id = i - UserConfig.get_total_orders()
            order_details.append(vars(OrderDetails(order_id, webinar_id, price)))


    return webinars_participants, order_details