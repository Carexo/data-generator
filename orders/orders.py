from data_generator import generate_inserts
from orders.courses.generate_participants_courses_and_orders import generate_participants_courses_and_orders
from orders.generate_orders import generate_order
from orders.meetings.generate_meetings_schedules_and_orders import generate_meetings_schedules_and_orders
from orders.studies.generate_participants_studies_and_orders import generate_participants_studies_and_orders
from orders.webinars.generate_webinar_participants_and_orders import generate_webinar_participants_and_orders

tables = {
    "Orders": ["OrderID", "BuyerID", "OrderDate", "PaymentDate", "PaymentPostponed", "PaymentUrl"],
    "WebinarsParticipants": ["WebinarID", "ParticipantID", "AvailableDue"],
    "MeetingsSchedules": ["MeetingID", "ParticipantID", "Presence"],
    "CoursesParticipants": ["CourseID", "ParticipantID"],
    "StudiesParticipants": ["StudyID", "ParticipantID"],
    "OrderDetails": ["OrderID", "ProductID", "Price"],
}

webinars_participants, order_details_webinars = generate_webinar_participants_and_orders()
meetings_schedules, order_details_meetings = generate_meetings_schedules_and_orders()
courses_participants, order_details_courses = generate_participants_courses_and_orders()
studies_participants, order_details_studies = generate_participants_studies_and_orders()

sample_data = {
    "Orders": generate_order(),
    "WebinarsParticipants": webinars_participants,
    "MeetingsSchedules": meetings_schedules,
    "CoursesParticipants": courses_participants,
    "StudiesParticipants": studies_participants,
    "OrderDetails": order_details_webinars + order_details_meetings + order_details_courses + order_details_studies,
}

generate_inserts(tables, sample_data, "orders_data.sql")