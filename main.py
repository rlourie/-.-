class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
            q += 1
        if q == 0:
            self.sr = 0
        else:
            self.sr = sum1 / q

    def __str__(self):
        self.sr_grade()
        result = f'Имя : {self.name}\nФамилия : {self.surname}\nСредняя оценка за лекции : {self.sr}'
        return result


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


Alex = Student('Alex', 'Zvezdin', 'M')
Alex.courses_in_progress += ['Python', 'SQL']

Oleg = Reviewer('Oleg', 'Buligin')
Oleg.courses_attached += ['Python', 'SQL']

Ne_Oleg = Lecturer('Ne_Oleg', 'Ne_Buligin')
Ne_Oleg.courses_attached += ['Python', 'SQL']

Oleg.rate_hw(Alex, 'Python', 10)
Oleg.rate_hw(Alex, 'Python', 10)
Oleg.rate_hw(Alex, 'Python', 10)
Alex.rate_lecture(Ne_Oleg, 'Python', 10)
Alex.rate_lecture(Ne_Oleg, 'Python', 9)
Alex.rate_lecture(Ne_Oleg, 'Python', 6)
Alex.rate_lecture(Ne_Oleg, 'SQL', 10)

print(Ne_Oleg)
print(Ne_Oleg.grades)
