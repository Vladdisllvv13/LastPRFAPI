import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class BaseStudent(BaseModel):
    """ Базовый класс для описания студента """

    firstname :str
    lastname :str
    login : str
    age :int
    birthdate :datetime.date
    id_group :str

class StudentIn(BaseStudent):
    """ Класс описывает студента, отправленный от пользователя """

    password :str


class StudentOut(BaseStudent):
    """ Класс описывает студента, который отправляется пользователю (без секретной информации) """

    id :str

class StudentStorage(BaseStudent):
    """ Класс описывает хранение студента в бд """

    id :str
    password :str