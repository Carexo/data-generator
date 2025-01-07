from config.product_config import ProductType, ProductsConfig


class StudyConfig:
    TOTAL_SUBJECTS = (ProductsConfig.get_products_ranges()[ProductType.STUDIES][1] - ProductsConfig.get_products_ranges()[ProductType.STUDIES][0] + 1) * 4


    @classmethod
    def get_total_subjects(cls):
        return cls.TOTAL_SUBJECTS