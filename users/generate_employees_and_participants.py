import random

from config.user_config import UserConfig, UserRoleType
from users.generate_users import random_phone
from utils.random_data import random_date


class Employee:
    def __init__(self, employee_id, employee_role_id, salary, work_phone):
        self.EmployeeID = employee_id
        self.EmployeeRoleID = employee_role_id
        self.Salary = salary
        self.WorkPhone = work_phone


class ParticipantsStudies:
    def __init__(self, participant_id, date_of_sign_up):
        self.ParticipantID = participant_id
        self.DateOfSignUp = date_of_sign_up


def generate_employees_and_participants():
    employees = []
    participants = []


    ranges = UserConfig.get_role_ranges()

    for key, value in ranges.items():
        if key == UserRoleType.PARTICIPANT:
            for i in range(value[0], value[1] + 1):
                participants.append(vars(ParticipantsStudies(i, random_date(2020, 2024).strftime("%Y-%m-%d %H:%M:%S"))))
        else:
            for i in range(value[0], value[1] + 1):
                salary = random.randint(2000, 10000)
                work_phone = random_phone()
                employees.append(vars(Employee(i, key.value, salary, work_phone)))

    return employees, participants