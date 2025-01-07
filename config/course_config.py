from enum import Enum

from config.product_config import ProductsConfig, ProductType


class ModuleType(Enum):
    ONLINE_SYNC = 1
    ONLINE_ASYNC = 2
    ON_SITE = 3
    HYBRID = 4


class CourseConfig:
    MODULE_PERCENTAGES = {
        ModuleType.ONLINE_SYNC: 0.2,
        ModuleType.ONLINE_ASYNC: 0.3,
        ModuleType.ON_SITE: 0.4,
        ModuleType.HYBRID: 0.1,
    }

    TOTAL_MODULES = (ProductsConfig.get_products_ranges()[ProductType.COURSE][1] - ProductsConfig.get_products_ranges()[ProductType.COURSE][0] + 1) * 4

    @classmethod
    def get_module_ranges(cls):
        ranges = {}
        start = 1

        for module_id, percentage in cls.MODULE_PERCENTAGES.items():
            end = start + int(cls.TOTAL_MODULES * percentage) - 1
            ranges[module_id] = (start, end)
            start = end + 1

        return ranges


