from enum import Enum

from config.product_config import ProductsConfig, ProductType


class MeetingFormType(Enum):
    STUDIES = 1
    COURSE = 2


class MeetingType(Enum):
    ONLINE_SYNC = 1
    ONLINE_ASYNC = 2
    ON_SITE = 3


class MeetingConfig:
    FORM_PERCENTAGES = {
        MeetingFormType.STUDIES: 0.6,
        MeetingFormType.COURSE: 0.4,
    }

    TYPE_PERCENTAGES = {
        MeetingType.ONLINE_SYNC: 0.6,
        MeetingType.ONLINE_ASYNC: 0.3,
        MeetingType.ON_SITE: 0.1,
    }

    TOTAL_ROOMS = (ProductsConfig.get_products_ranges()[ProductType.MEETING][1] - ProductsConfig.get_products_ranges()[ProductType.MEETING][0] + 1) // 2

    @classmethod
    def get_meeting_range(cls):
        meetings = ProductsConfig.get_products_ranges()[ProductType.MEETING]
        meeting_ranges = {}

        total_meetings = meetings[1] - meetings[0] + 1
        start = meetings[0]

        for form, form_percentage in cls.FORM_PERCENTAGES.items():
            form_total = int(total_meetings * form_percentage)
            form_start = start
            form_end = form_start + form_total - 1

            meeting_ranges[form] = {}

            type_start = form_start
            for meeting_type, type_percentage in cls.TYPE_PERCENTAGES.items():
                type_total = int(form_total * type_percentage)
                type_end = type_start + type_total - 1
                meeting_ranges[form][meeting_type] = (type_start, type_end)
                type_start = type_end + 1

            start = form_end + 1

        return meeting_ranges

    @classmethod
    def get_total_rooms(cls):
        return cls.TOTAL_ROOMS