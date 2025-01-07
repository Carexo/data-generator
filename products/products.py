from config.product_config import ProductType
from data_generator import generate_inserts
from products.generate_products import generate_products
from products.webinars.generate_webinars import generate_webinars

tables = {
    "ProductType": ["ProductTypeID", "Type"],
    "Products": ["ProductID", "Price", "Active", "Type", "RegularDiscount"],
    "Webinars": ["WebinarID", "Name", "VideoLink", "Date", "Duration", "Description", "TranslationID", "TutorID"],
}


sample_data = {
    "ProductType": [
        {"ProductTypeID": ProductType.WEBINAR.value, "Type": "Webinar"},
        {"ProductTypeID": ProductType.COURSE.value, "Type": "Kurs"},
        {"ProductTypeID": ProductType.STUDIES.value, "Type": "Studia"},
        {"ProductTypeID": ProductType.MEETING.value, "Type": "Spotkanie"},
    ],
    "Products": generate_products(),
    "Webinars": generate_webinars(),
}


generate_inserts(tables, sample_data, "products_data.sql")

