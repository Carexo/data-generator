import random

from config.product_config import ProductsConfig, ProductType
from config.user_config import UserConfig, UserRoleType
from utils.random_data import random_date, random_duration


class Webinar:
    def __init__(self, WebinarID, Name, VideoLink, Date, Duration, Description, TranslationID, TutorID):
        self.WebinarID = WebinarID
        self.Name = Name
        self.VideoLink = VideoLink
        self.Date = Date
        self.Duration = Duration
        self.Description = Description
        self.TranslationID = TranslationID
        self.TutorID = TutorID


webinar_names = [
    "Introduction to Python",
    "Advanced Machine Learning",
    "Data Science with R",
    "Web Development with Django",
    "Cloud Computing Essentials",
    "Digital Marketing Strategies",
    "Effective Communication Skills",
    "Time Management Techniques",
    "Introduction to Graphic Design",
    "Basics of Financial Planning",
    "Public Speaking Mastery",
    "Creative Writing Workshop",
    "Photography Basics",
    "Introduction to Yoga",
    "Mindfulness and Meditation",
    "Personal Finance Management",
    "Healthy Eating Habits",
    "Introduction to Music Theory",
    "Basics of Gardening",
    "Travel Planning Tips"
]

descriptions = [
    "Learn the basics of Python programming.",
    "Explore advanced techniques in machine learning.",
    "Master data science using the R programming language.",
    "Build web applications using the Django framework.",
    "Understand the fundamentals of cloud computing.",
    "Discover strategies for successful digital marketing.",
    "Improve your communication skills for better interactions.",
    "Learn techniques to manage your time effectively.",
    "Get started with graphic design principles and tools.",
    "Understand the basics of financial planning and management.",
    "Master the art of public speaking.",
    "Enhance your creative writing skills.",
    "Learn the basics of photography.",
    "Get introduced to the practice of yoga.",
    "Practice mindfulness and meditation techniques.",
    "Manage your personal finances effectively.",
    "Adopt healthy eating habits.",
    "Learn the basics of music theory.",
    "Start your journey into gardening.",
    "Get tips for planning your travels."
]

def generate_webinars():
    webinars = []
    tutor_range = UserConfig.get_role_ranges()[UserRoleType.TUTOR]
    webinar_range = ProductsConfig.get_products_ranges()[ProductType.WEBINAR]
    for i in range(webinar_range[0], webinar_range[1] + 1):
        name = random.choice(webinar_names)
        video_link = f"https://example.com/{name.replace(' ', '_')}"
        date = random_date(2023, 2027).strftime("%Y-%m-%d %H:%M:%S")
        duration = None if random.random() < 0.5 else random_duration()
        description = None if random.random() < 0.1 else random.choice(descriptions)
        translation_id = None if random.random() < 0.7 else random.randint(1, UserConfig.get_total_translations())
        tutor_id = random.randint(tutor_range[0], tutor_range[1])

        webinars.append(
            vars(Webinar(i, name, video_link, date, duration, description, translation_id, tutor_id)))

    return webinars