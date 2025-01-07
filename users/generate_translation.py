import random
from config.user_config import UserRoleType, UserConfig


class Translation:
    def __init__(self, TranslationID, LanguageID, TranslatorID):
        self.TranslationID = TranslationID
        self.LanguageID = LanguageID
        self.TranslatorID = TranslatorID

def generate_translations():
    translations = []
    translators_range = UserConfig.get_role_ranges()[UserRoleType.TRANSLATOR]
    for i in range(1, UserConfig.get_total_translations() + 1):
        language_id = random.randint(1, 10)
        translator_id = random.randint(translators_range[0], translators_range[1])
        translations.append(vars(Translation(i, language_id, translator_id)))

    return translations