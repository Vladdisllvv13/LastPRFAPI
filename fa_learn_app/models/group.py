import uuid
from pydantic import BaseModel


class BaseGroup(BaseModel):
    """ Базовый класс для описания группы """

    name :str


class GroupStorage(BaseGroup):
    """ Класс описывает хранение группы в бд """

    id :str