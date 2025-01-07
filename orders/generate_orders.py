import random
from datetime import datetime, timedelta

from config.user_config import UserRoleType, UserConfig
from utils.random_data import random_date


class Orders:
    def __init__(self, order_id, buyer_id, order_date, payment_date, payment_postponed, payment_url):
        self.OrderID = order_id
        self.BuyerID = buyer_id
        self.OrderDate = order_date
        self.PaymentDate = payment_date
        self.PaymentPostponed = payment_postponed
        self.PaymentUrl = payment_url

class OrderDetails:
    def __init__(self, order_id, product_id, price):
        self.OrderID = order_id
        self.ProductID = product_id
        self.Price = price


def generate_order():
    orders = []

    participants_range = UserConfig.get_role_ranges()[UserRoleType.PARTICIPANT]

    for i in range(participants_range[0], participants_range[1] + 1):
        order_id = i - UserConfig.get_total_orders()
        buyer_id = i
        order_date = random_date(2020, 2024).strftime("%Y-%m-%d %H:%M:%S")
        payment_postponed = 0 if random.random() < 0.9 else 1

        random_number = random.random()

        if random_number < 0.1:
            payment_date = None
        elif random_number < 0.3:
            payment_date = (datetime.strptime(order_date, "%Y-%m-%d %H:%M:%S") + timedelta(days=random.randint(1, 10))).strftime(
                "%Y-%m-%d %H:%M:%S")
        else:
            payment_date = order_date

        payment_url = f"https://www.example.com/payment/{buyer_id * order_id}/{order_date.replace('-', '')}"

        orders.append(vars(Orders(order_id, buyer_id, order_date, payment_date, payment_postponed, payment_url)))

    return orders
