import file_operations
from faker import Faker
import random
import os


SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]


LETTERS = {
    "а": "а͠",
    "б": "б̋",
    "в": "в͒͠",
    "г": "г͒͠",
    "д": "д̋",
    "е": "е͠",
    "ё": "ё͒͠",
    "ж": "ж͒",
    "з": "з̋̋͠",
    "и": "и",
    "й": "й͒͠",
    "к": "к̋̋",
    "л": "л̋͠",
    "м": "м͒͠",
    "н": "н͒",
    "о": "о̋",
    "п": "п̋͠",
    "р": "р̋͠",
    "с": "с͒",
    "т": "т͒",
    "у": "у͒͠",
    "ф": "ф̋̋͠",
    "х": "х͒͠",
    "ц": "ц̋",
    "ч": "ч̋͠",
    "ш": "ш͒͠",
    "щ": "щ̋",
    "ъ": "ъ̋͠",
    "ы": "ы̋͠",
    "ь": "ь̋",
    "э": "э͒͠͠",
    "ю": "ю̋͠",
    "я": "я̋",
    "А": "А͠",
    "Б": "Б̋",
    "В": "В͒͠",
    "Г": "Г͒͠",
    "Д": "Д̋",
    "Е": "Е",
    "Ё": "Ё͒͠",
    "Ж": "Ж͒",
    "З": "З̋̋͠",
    "И": "И",
    "Й": "Й͒͠",
    "К": "К̋̋",
    "Л": "Л̋͠",
    "М": "М͒͠",
    "Н": "Н͒",
    "О": "О̋",
    "П": "П̋͠",
    "Р": "Р̋͠",
    "С": "С͒",
    "Т": "Т͒",
    "У": "У͒͠",
    "Ф": "Ф̋̋͠",
    "Х": "Х͒͠",
    "Ц": "Ц̋",
    "Ч": "Ч̋͠",
    "Ш": "Ш͒͠",
    "Щ": "Щ̋",
    "Ъ": "Ъ̋͠",
    "Ы": "Ы̋͠",
    "Ь": "Ь̋",
    "Э": "Э͒͠͠",
    "Ю": "Ю̋͠",
    "Я": "Я̋",
    " ": " ",
}


def do_things():
    fake = Faker("ru_RU")
    fake_name = fake.first_name()
    fake_surname = fake.last_name()
    fake_job = fake.job()
    fake_city = fake.city()
    random_strengt = random.randint(3, 18)
    random_agility = random.randint(3, 18)
    random_endurance = random.randint(3, 18)
    random_int = random.randint(3, 18)
    random_luck = random.randint(3, 18)
    skills_random = random.sample(SKILLS, 3)

    runic_skills = []

    for skill in skills_random:
        runic_skill = skill
        for original_letter in LETTERS:
            magic_letter = LETTERS[original_letter]
            runic_skill = runic_skill.replace(original_letter, magic_letter)
        runic_skills.append(runic_skill)

    context = {
        "first_name": fake_name,
        "last_name": fake_surname,
        "job": fake_job,
        "town": fake_city,
        "strength": random_strengt,
        "agility": random_agility,
        "endurance": random_endurance,
        "intelligence": random_int,
        "luck": random_luck,
        "skill_1": runic_skills[0],
        "skill_2": runic_skills[1],
        "skill_3": runic_skills[2],
    }

    os.makedirs(os.path.join("output", "svg"), exist_ok=True)

    return context


def main():
    for number in range(10):
        save_path = os.path.join("output", "svg", "result{n}.svg".format(n=number))
        file_operations.render_template("src/charsheet.svg", save_path, do_things())


if __name__ == "__main__":
    main()
