from config.meeting_config import MeetingFormType, MeetingType
from data_generator import generate_inserts
from products.meetings_generator.generate_meetings import generate_meetings
from products.meetings_generator.generate_rooms import generate_rooms

tables = {
    "FormType": ["FormTypeID", "Type"],
    "MeetingTypes": ["MeetingTypeID", "Type"],
    "Classrooms": ["RoomID", "Capacity", "Building", "RoomName"],
    "Meetings": [
        "MeetingID", "Date", "Duration", "FormTypeID",
        "TranslationID", "TutorID", "MeetingTypeID", "SubjectID", "ModuleID"
    ],
    "OnSiteMeetings": ["MeetingID", "RoomID", "LimitPlaces"],
    "OnlineAsyncMeetings": ["MeetingID", "VideoLink"],
    "OnlineSyncMeetings": ["MeetingID", "MeetingLink"],
}


data = generate_meetings()

sample_data = {
    "FormType": [
        {"FormTypeID": MeetingFormType.STUDIES.value, "Type": "studia"},
        {"FormTypeID": MeetingFormType.COURSE.value, "Type": "kurs"},
    ],
    "MeetingTypes": [
        {"MeetingTypeID": MeetingType.ONLINE_SYNC.value, "Type": "online-synchroniczne"},
        {"MeetingTypeID": MeetingType.ONLINE_ASYNC.value, "Type": "online-asynchroniczne"},
        {"MeetingTypeID": MeetingType.ON_SITE.value, "Type": "stacjonarne"},
    ],
    "Classrooms": generate_rooms(),
    "Meetings": data["meetings"],
    "OnSiteMeetings": data[MeetingType.ON_SITE],
    "OnlineAsyncMeetings": data[MeetingType.ONLINE_ASYNC],
    "OnlineSyncMeetings": data[MeetingType.ONLINE_SYNC],
}
generate_inserts(tables, sample_data, "meetings_data.sql")
