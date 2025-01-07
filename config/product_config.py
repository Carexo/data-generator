from enum import Enum

class ProductType(Enum):
    WEBINAR = 1
    COURSE = 2
    STUDIES = 3
    MEETING = 4

class ProductsConfig:
    ROLE_PERCENTAGES = {
        ProductType.WEBINAR: 0.1,
        ProductType.COURSE: 0.15,
        ProductType.STUDIES: 0.05,
        ProductType.MEETING: 0.7,
    }

    TOTAL_PRODUCTS = 5000

    @classmethod
    def get_products_ranges(cls):
        ranges = {}
        start = 1  # Start from 1 instead of 0
        for role_id, percentage in cls.ROLE_PERCENTAGES.items():
            end = start + int(cls.TOTAL_PRODUCTS * percentage) - 1
            ranges[role_id] = (start, end)
            start = end + 1

        return ranges

    @classmethod
    def get_total(cls):
        return cls.TOTAL_PRODUCTS
