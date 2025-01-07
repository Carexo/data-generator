import random

from config.product_config import ProductsConfig, ProductType
from config.user_config import UserConfig
from orders.generate_orders import OrderDetails


class CoursesParticipants:
    def __init__(self, course_id, participant_id):
        self.CourseID = course_id
        self.ParticipantID = participant_id

def generate_participants_courses_and_orders():
    courses_participants = []
    order_details = []
    existing_pairs = set()

    participants_courses_ranges = UserConfig.get_product_ranges()[ProductType.COURSE]
    course_range = ProductsConfig.get_products_ranges()[ProductType.COURSE]

    for participants_courses_range in participants_courses_ranges:
        for i in range(participants_courses_range[0], participants_courses_range[1] + 1):
            course_id = random.randint(course_range[0], course_range[1])

            if (course_id, i) in existing_pairs:
                continue

            courses_participants.append(vars(CoursesParticipants(course_id, i)))
            existing_pairs.add((course_id, i))

            price = random.randint(50, 500)
            order_id = i - UserConfig.get_total_orders()
            order_details.append(vars(OrderDetails(order_id, course_id, price)))

    return courses_participants, order_details
