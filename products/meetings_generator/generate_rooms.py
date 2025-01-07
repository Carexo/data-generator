import time
import random

from config.meeting_config import MeetingConfig


class Classroom:
    def __init__(self, RoomID, Capacity, Building, RoomName):
        self.RoomID = RoomID
        self.Capacity = Capacity
        self.Building = Building
        self.RoomName = RoomName


def generate_rooms():
    rooms = []
    for i in range(1, MeetingConfig.get_total_rooms()):
        capacity = random.randint(10, 100)
        building = random.choice(["A", "B", "C", "D", "E", "F"])
        unique_id = int(time.time() * 1000) + i  # Adding a unique identifier based on the current time
        room_name = f"{building}{random.randint(1, 100)}_{unique_id}"
        rooms.append(vars(Classroom(i, capacity, building, room_name)))

    return rooms