from fa_learn_app.repositories.student import StudentTmpRepository

TMP_STUDENT_REPOSITORY = StudentTmpRepository()

def get_student_repo() -> StudentTmpRepository:
    """ Получение student репозитория """

    return TMP_STUDENT_REPOSITORY