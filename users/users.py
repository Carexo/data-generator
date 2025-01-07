from config.user_config import UserRoleType
from data_generator import generate_inserts
from users.generate_translation import generate_translations
from users.generate_users import generate_users
from users.generate_employees_and_participants import generate_employees_and_participants

tables = {
    "Users": [
        "UserID", "FirstName", "LastName", "Email", "PersonalPhone",
        "DateOfBirth", "AddressID", "Active"
    ],
    "EmployeeRoles": ["RoleID", "Type"],
    "Employees": ["EmployeeID", "EmployeeRoleID", "Salary", "WorkPhone"],
    "Participants": ["ParticipantID", "DateOfSignUp"],
    "Languages": ["LanguageID", "LanguageName"],
    "Translations": ["TranslationID", "LanguageID", "TranslatorID"],
}

employees, participants = generate_employees_and_participants()

sample_data = {
    "EmployeeRoles": [
        {"RoleID": UserRoleType.ADMINISTRATOR.value, "Type": "Administrator"},
        {"RoleID": UserRoleType.ACCOUNTANT.value, "Type": "Księgowy"},
        {"RoleID": UserRoleType.ADMINISTRATOR_SECRETARIAT.value, "Type": "Administrator - sekretariat"},
        {"RoleID": UserRoleType.COORDINATOR.value, "Type": "Koordynator"},
        {"RoleID": UserRoleType.PLANNER.value, "Type": "Planista"},
        {"RoleID": UserRoleType.TRANSLATOR.value, "Type": "Tłumacz"},
        {"RoleID": UserRoleType.TUTOR.value, "Type": "Prowadzący"},
        {"RoleID": UserRoleType.DIRECTOR.value, "Type": "Dyrektor"}],
    "Users": generate_users(),
    "Employees": employees,
    "Participants": participants,
    "Languages": [
        {"LanguageID": 1, "LanguageName": "Angielski"},
        {"LanguageID": 2, "LanguageName": "Polski"},
        {"LanguageID": 3, "LanguageName": "Hiszpański"},
        {"LanguageID": 4, "LanguageName": "Niemiecki"},
        {"LanguageID": 5, "LanguageName": "Francuski"},
        {"LanguageID": 6, "LanguageName": "Włoski"},
        {"LanguageID": 7, "LanguageName": "Portugalski"},
        {"LanguageID": 8, "LanguageName": "Rosyjski"},
        {"LanguageID": 9, "LanguageName": "Chiński"},
        {"LanguageID": 10, "LanguageName": "Japoński"},
    ],
    "Translations": generate_translations()
}

generate_inserts(tables, sample_data, "users_data.sql")