import random

from enum import Enum

from config.product_config import ProductType


class UserRoleType(Enum):
    ADMINISTRATOR = 1
    ACCOUNTANT = 2
    ADMINISTRATOR_SECRETARIAT = 3
    COORDINATOR = 4
    PLANNER = 5
    TRANSLATOR = 6
    TUTOR = 7
    DIRECTOR = 8
    PARTICIPANT = 9


class UserConfig:
    ROLE_PERCENTAGES = {
        UserRoleType.ADMINISTRATOR: 0.01,
        UserRoleType.ACCOUNTANT: 0.02,
        UserRoleType.ADMINISTRATOR_SECRETARIAT: 0.02,
        UserRoleType.COORDINATOR: 0.10,
        UserRoleType.PLANNER: 0.05,
        UserRoleType.TRANSLATOR: 0.10,
        UserRoleType.TUTOR: 0.70,
    }

    TOTAL_PARTICIPANTS = 5000
    TOTAL_EMPLOYEES = 800
    TOTAL_TRANSLATIONS = 200

    @classmethod
    def get_role_ranges(cls):
        ranges = {}
        start = 1  # Start from 1 instead of 0
        for role_id, percentage in cls.ROLE_PERCENTAGES.items():
            end = start + int(cls.TOTAL_EMPLOYEES * percentage) - 1
            ranges[role_id] = (start, end)
            start = end + 1

        # Ensure UserRoleType.DIRECTOR always has one ID
        director_id = UserRoleType.DIRECTOR
        ranges[director_id] = (cls.TOTAL_EMPLOYEES + 1, cls.TOTAL_EMPLOYEES + 1)

        ranges[UserRoleType.PARTICIPANT] = (cls.TOTAL_EMPLOYEES + 2, cls.TOTAL_EMPLOYEES + 2 + cls.TOTAL_PARTICIPANTS)

        return ranges

    @classmethod
    def get_product_ranges(cls):
        random.seed(2137)

        product_ranges = {ProductType.WEBINAR: [], ProductType.COURSE: [], ProductType.STUDIES: [], ProductType.MEETING: []}
        participant_range = cls.get_role_ranges()[UserRoleType.PARTICIPANT]
        total_participants = cls.TOTAL_PARTICIPANTS
        start, end = participant_range

        product_ranges[ProductType.WEBINAR].append((start, start + total_participants // 4))
        product_ranges[ProductType.COURSE].append((start + total_participants // 5, start + total_participants // 3))
        product_ranges[ProductType.STUDIES].append((start + total_participants // 4, start + total_participants // 2))
        product_ranges[ProductType.MEETING].append((start + total_participants // 3, end))

        for _ in range(6):
            for product_type in ProductType:
                range_start = random.randint(start, end)
                range_end = random.randint(range_start, end)
                product_ranges[product_type].append((range_start, range_end))


        for _ in range(20):
            range_start = random.randint(start, end)
            range_end = random.randint(range_start, end)

            product_ranges[ProductType.MEETING].append((range_start, range_end))

        for _ in range(20):
            range_start = random.randint(start, end)
            range_end = random.randint(range_start, end)

            product_ranges[ProductType.COURSE].append((range_start, range_end))

        for _ in range(20):
            range_start = random.randint(start, end)
            range_end = random.randint(range_start, end)

            product_ranges[ProductType.STUDIES].append((range_start, range_end))

        return product_ranges


    @classmethod
    def get_total_users(cls):
        return cls.TOTAL_EMPLOYEES + cls.TOTAL_PARTICIPANTS + 2

    @classmethod
    def get_total_orders(cls):
        return cls.TOTAL_EMPLOYEES

    @classmethod
    def get_total_translations(cls):
        return cls.TOTAL_TRANSLATIONS