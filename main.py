FORMAT = ...
WEIGHT = ...  # Вес
HEIGHT = ...  # Рост
K_1 = ...  # Коэффициент для подсчета калорий
K_2 = ...  # Коэффициент для подсчета калорий
STEP_M = ...  # Длина шага в метрах


def check_correct_data(data):
    """Проверка корректности полученного пакета."""


def check_correct_time(time):
    """Проверка корректности параметра времени."""


def get_step_day(steps):
    """Получить количество пройденных шагов за день."""


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""


def show_message(time, steps, dist, calories, achiev):
    """Вывести на экран результаты вычислений"""


def accept_package(data):
    """Обработать пакет данных."""


if __name__ == '__main__':
    # Пример запуска
    ...
