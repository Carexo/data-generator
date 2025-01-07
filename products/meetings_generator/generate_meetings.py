import random

from config.course_config import ModuleType, CourseConfig
from config.meeting_config import MeetingConfig, MeetingType, MeetingFormType
from config.study_config import StudyConfig
from config.user_config import UserConfig, UserRoleType
from utils.random_data import random_date, random_duration

class Meeting:
    def __init__(self, MeetingID, Date, Duration, FormTypeID, TranslationID, TutorID, MeetingTypeID, SubjectID, ModuelID):
        self.MeetingID = MeetingID
        self.Date = Date
        self.Duration = Duration
        self.FormTypeID = FormTypeID
        self.TranslationID = TranslationID
        self.TutorID = TutorID
        self.MeetingTypeID = MeetingTypeID
        self.SubjectID = SubjectID
        self.ModuleID = ModuelID


class OnSiteMeeting:
    def __init__(self, MeetingID, RoomID, LimitPlaces):
        self.MeetingID = MeetingID
        self.RoomID = RoomID
        self.LimitPlaces = LimitPlaces

class OnlineAsyncMeeting:
    def __init__(self, MeetingID, VideoLink):
        self.MeetingID = MeetingID
        self.VideoLink = VideoLink

class OnlineSyncMeeting:
    def __init__(self, MeetingID, MeetingLink):
        self.MeetingID = MeetingID
        self.MeetingLink = MeetingLink

def generate_meetings():
    data = {
        "meetings" : [],
        MeetingType.ON_SITE : [],
        MeetingType.ONLINE_SYNC : [],
        MeetingType.ONLINE_ASYNC: []
    }

    meetings_range = MeetingConfig.get_meeting_range()

    tutor_range = UserConfig.get_role_ranges()[UserRoleType.TUTOR]

    course_module_ranges = CourseConfig.get_module_ranges()
    course_iterator = {
        ModuleType.ONLINE_SYNC: {"range_values": course_module_ranges[ModuleType.ONLINE_SYNC], "i": course_module_ranges[ModuleType.ONLINE_SYNC][0]},
        ModuleType.ONLINE_ASYNC: {"range_values": course_module_ranges[ModuleType.ONLINE_ASYNC], "i": course_module_ranges[ModuleType.ONLINE_ASYNC][0]},
        ModuleType.ON_SITE: {"range_values": course_module_ranges[ModuleType.ON_SITE], "i": course_module_ranges[ModuleType.ON_SITE][0]},
        ModuleType.HYBRID: {"range_values": course_module_ranges[ModuleType.HYBRID], "i": course_module_ranges[ModuleType.HYBRID][0]},
    }

    for form_type, value in meetings_range.items():
        for meeting_type, range_value in value.items():
            for i in range(range_value[0],  range_value[1] + 1):
                date = random_date(2023, 2027).strftime("%Y-%m-%d %H:%M:%S")
                duration = None if random.random() < 0.7 else random_duration()
                form_type_id = form_type.value
                translation_id = None if random.random() < 0.8 else random.randint(1, UserConfig.get_total_translations())
                tutor_id = random.randint(tutor_range[0], tutor_range[1])
                meeting_type_id = meeting_type.value


                if meeting_type == MeetingType.ON_SITE:
                    limit_places = random.randint(10, 50)
                    room_id = random.randint(1, MeetingConfig.get_total_rooms())
                    onsite_meeting = OnSiteMeeting(i, room_id, limit_places)
                    data[MeetingType.ON_SITE].append(vars(onsite_meeting))
                elif meeting_type == MeetingType.ONLINE_ASYNC:
                    video_link = f"https://www.youtube.com/watch?v={i}"
                    online_async_meeting = OnlineAsyncMeeting(i, video_link)
                    data[MeetingType.ONLINE_ASYNC].append(vars(online_async_meeting))
                elif meeting_type == MeetingType.ONLINE_SYNC:
                    meeting_link = f"https://www.zoom.com/meeting/{i}"
                    online_sync_meeting = OnlineSyncMeeting(i, meeting_link)
                    data[MeetingType.ONLINE_SYNC].append(vars(online_sync_meeting))

                if form_type == MeetingFormType.COURSE:
                    module_type = ModuleType.HYBRID
                    if meeting_type == MeetingType.ONLINE_SYNC:
                        module_type = ModuleType.HYBRID if random.random() < 0.2 else ModuleType.ONLINE_SYNC
                    if meeting_type == MeetingType.ONLINE_ASYNC:
                        module_type = ModuleType.HYBRID if random.random() < 0.2 else ModuleType.ONLINE_ASYNC
                    if meeting_type == MeetingType.ON_SITE:
                        module_type = ModuleType.HYBRID if random.random() < 0.2 else ModuleType.ON_SITE

                    topic_id_1 = course_iterator[module_type]["i"]
                    course_iterator[module_type]["i"] += 1
                    if course_iterator[module_type]["i"] > course_iterator[module_type]["range_values"][1]:
                        course_iterator[module_type]["i"] = course_iterator[module_type]["range_values"][0]

                    meeting = Meeting(i, date, duration, form_type_id, translation_id, tutor_id,
                                          meeting_type_id, None, topic_id_1)

                    data["meetings"].append(vars(meeting))
                elif form_type == MeetingFormType.STUDIES:
                    # TODO: change when some subject is generated without meeting
                    topic_id_2 = random.randint(1, StudyConfig.get_total_subjects())
                    meeting = Meeting(i, date, duration, form_type_id, translation_id, tutor_id,
                                      meeting_type_id, topic_id_2, None)

                    data["meetings"].append(vars(meeting))

    return data