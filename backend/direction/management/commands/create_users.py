from users.models import User, UserCourses, UserGradeMap
from direction.models import Course, Profession
from pprint import pprint
from django.shortcuts import get_object_or_404


USERS = [
    "ivan@mail.ru",
    "jenifer@mail.ru",
    "konstantin@mail.ru",
]


def create_users():
    try:
        User.objects.get_or_create(
            email="ivan@mail.ru", username="Ivan", password="testivan"
        ),
        User.objects.get_or_create(
            email="jenifer@mail.ru",
            username="Jenifer",
            password="jenitest",
        ),
        User.objects.get_or_create(
            email="konstantin@mail.ru",
            username="Konstantin",
            password="konstantin",
        ),
        User.objects.get_or_create(
            email="admin@mail.ru",
            username="admin",
            password="admin",
            is_staff=True,
        ),

        pprint("Пользователи добавлены")
    except Exception as err:
        pprint(f"ошибка добавления пользователей : {err} ")


def create_user_course_relation():
    users = []
    for x in USERS:
        users.append(get_object_or_404(User, email=x))
    course1 = get_object_or_404(Course, id=13)
    course2 = get_object_or_404(Course, id=19)
    UserCourses.objects.get_or_create(
        user=users[0], course=course1, status="passed"
    )
    UserCourses.objects.get_or_create(
        user=users[2], course=course2, status="in_progress"
    )


def create_user_grade_map():
    users = []
    for x in USERS:
        users.append(get_object_or_404(User, email=x))
    prof1 = get_object_or_404(Profession, id=6)
    prof2 = get_object_or_404(Profession, id=1)
    prof3 = get_object_or_404(Profession, id=4)

    try:
        user1 = UserGradeMap.objects.get_or_create(
            user=users[0],
            start_level="middle",
            end_level="senior",
            start_prof=prof1,
            end_prof=prof1,
        )
        pprint(f"карта {user1} добавлена")
        user2 = UserGradeMap.objects.get_or_create(
            user=users[1],
            start_level="newbie",
            end_level="junior",
            end_prof=prof2,
        )
        pprint(f"карта {user2} добавлена")

        user3 = UserGradeMap.objects.get_or_create(
            user=users[2],
            start_level="senior",
            end_level="lead",
            start_prof=prof3,
            end_prof=prof3,
        )
        pprint(f"карта {user3} добавлена")

    except Exception as err:
        pprint(f"ошибка добавления карты пользователей : {err} ")
