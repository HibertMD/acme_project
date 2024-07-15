from datetime import date

from django.core.exceptions import ValidationError


def real_age(value, min_age=0, max_age=120):
    age = (date.today() - value).days / 365
    if age < min_age or age > max_age:
        raise ValidationError(
            f'Ожидается возраст от {min_age} до {max_age}'
        )