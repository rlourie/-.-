class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sr = 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print("Ошибка")
            return

    def __str__(self):
        Lecturer.sr_grade(self)
        result = f'Имя : {self.name}\nФамилия : {self.surname}\nСредняя оценка за дз : {self.sr}\n' \
                 f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n' \
                 f'Завершенные курсы: {"".join(self.finished_courses)}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не студент")
            return
        return self.sr < other.sr


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.sr = 0

    def sr_grade(self):
        sum1 = 0
        q = 0
        dict = self.grades
        for _, value in dict.items():
            sum1 += sum(value)
            q += len(value)
        if q == 0:
            self.sr = 0
        else:
            self.sr = sum1 / q

    def __str__(self):
        self.sr_grade()
        result = f'Имя : {self.name}\nФамилия : {self.surname}\nСредняя оценка за лекции : {self.sr}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не лектор")
            return
        return self.sr < other.sr


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print("Ошибка")
            return 'Ошибка'

    def __str__(self):
        result = f'Имя : {self.name}\nФамилия : {self.surname}'
        return result


def sr_mark_student(list_students, name_course):
    q = 0
    summ = 0
    for student in list_students:
        grade_dict = student.grades
        for key, value in grade_dict.items():
            if key == name_course:
                summ += sum(value)
                q += len(value)
    if q == 0:
        return 0
    else:
        return summ / q


def sr_mark_lecture(list_lecturer, name_course):
    q = 0
    summ = 0
    for lecturer in list_lecturer:
        grade_dict = lecturer.grades
        for key, value in grade_dict.items():
            if key == name_course:
                summ += sum(value)
                q += len(value)
    if q == 0:
        return 0
    else:
        return summ / q


Alex = Student('Alex', 'Zvezdin', 'M')
Alex.courses_in_progress += ['Python', 'SQL']
Alex.finished_courses += ['Django']

Artem = Student('Artem', 'Zvezdin1', 'M')
Artem.courses_in_progress += ['Python', 'SQL']
Artem.finished_courses += ['Django']

Oleg = Reviewer('Oleg', 'Buligin')
Oleg.courses_attached += ['Python', 'SQL']

Ne_Oleg = Lecturer('Ne_Oleg', 'Ne_Buligin')
Ne_Oleg.courses_attached += ['Python', 'SQL']

Artemiy = Lecturer('Artemiy', 'Ne_Buligin')
Artemiy.courses_attached += ['Python', 'SQL']

Oleg.rate_hw(Alex, 'Python', 10)
Oleg.rate_hw(Alex, 'Python', 2)
Oleg.rate_hw(Alex, 'Python', 8)
Oleg.rate_hw(Alex, 'SQL', 9)

Oleg.rate_hw(Artem, 'Python', 2)
Oleg.rate_hw(Artem, 'Python', 2)
Oleg.rate_hw(Artem, 'Python', 2)
Oleg.rate_hw(Artem, 'SQL', 2)

Alex.rate_lecture(Ne_Oleg, 'Python', 10)
Alex.rate_lecture(Ne_Oleg, 'Python', 9)
Alex.rate_lecture(Ne_Oleg, 'Python', 6)
Alex.rate_lecture(Ne_Oleg, 'SQL', 10)

Alex.rate_lecture(Artemiy, 'Python', 0)
Alex.rate_lecture(Artemiy, 'Python', 9)
Alex.rate_lecture(Artemiy, 'Python', 6)
Alex.rate_lecture(Artemiy, 'SQL', 10)

print(Ne_Oleg)
print(Ne_Oleg.grades)

print()

print(Oleg)

print()

print(Alex)
print(Alex.grades)

print()

print(Alex > Artem)
print(Artemiy > Ne_Oleg)

print()

print(sr_mark_student([Alex, Artem], "Python"))
print(sr_mark_lecture([Ne_Oleg, Artemiy], "Python"))
