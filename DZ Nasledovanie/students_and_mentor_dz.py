class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        sum_ = 0
        len_ = 0
        for i in self.grades.values():
            sum_ += sum(i)
            len_ += len(i)
        result = round(sum_ / len_, 2)
        return result

    def average_rate_course(self, course):
        sum_courses = 0
        len_courses = 0
        for courses in self.grades.keys():
            if courses == course:
                sum_courses += sum(self.grades[course])
                len_courses += len(self.grades[course])
        result = round(sum_courses / len_courses, 2)
        return result

    def __str__(self):
        result = f"Имя: {self.name}\n" \
            f"Фамилия: {self.surname}\n" \
            f"Средняя оценка за домашние задания: {self.average_rate()}\n" \
            f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n" \
            f"Завершенные курсы: {", ".join(self.finished_courses)}\n"
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Сравнение невозможно.")
            return
        return self.average_rate() < other.average_rate()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate(self):
        sum_ = 0
        len_ = 0
        for y in self.grades.values():
            sum_ += sum(y)
            len_ += len(y)
        result = round(sum_ / len_, 2)
        return result

    def average_rate_course(self, course):
        sum_courses = 0
        len_courses = 0
        for course in self.grades.keys():
            sum_courses += sum(self.grades[course])
            len_courses += len(self.grades[course])
        result = round(sum_courses / len_courses, 2)
        return result

    def __str__(self):
        result = (f"Имя: {self.name}\nФамилия: {self.surname}\n" 
                  f"Средняя оценка за лекции: {self.average_rate()}\n")
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Разные категории объектов не сравниваем")
            return
        return self.average_rate() < other.average_rate()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        result = (f"Имя: {self.name}\n"
                  f"Фамилия: {self.surname}\n")
        return result

student_01 = Student("Natalia", "Barabanova", "Woman")
student_01.courses_in_progress = ["Python", "Git"]
student_01.finished_courses = ["Java"]

student_02 = Student("Ruoy", "Eman", "Man")
student_02.finished_courses = ["Git", "C++"]
student_02.courses_in_progress = ["Python", "Java"]

reviewer_01 = Reviewer("Some", "Buddy")
reviewer_01.courses_attached += ["Python", "C++", "Java"]

reviewer_02 = Reviewer("Elvis", "Presley")
reviewer_02.courses_attached += ["Python", "Git"]

lecturer_01 = Lecturer("Some", "Buddy")
lecturer_02 = Lecturer("John", "Lennon")

reviewer_01.rate_hw(student_01, "Python", 10)
reviewer_01.rate_hw(student_02, "Python", 10)
reviewer_02.rate_hw(student_01, "Python", 10)
reviewer_02.rate_hw(student_02, "Python", 8)

student_01.rate_lect(lecturer_01, "Python", 10)
student_01.rate_lect(lecturer_02, "Python", 10)
student_02.rate_lect(lecturer_01, "Python", 10)
student_02.rate_lect(lecturer_02, "Python", 9)

student_list = [student_01, student_02]
lector_list = [lecturer_01, lecturer_02]

import gc

print("Список экспертов")
for obj in gc.get_objects():
    if isinstance(obj, Reviewer):
        print(obj)

print("Список лекторов")
for obj in gc.get_objects():
    if isinstance(obj, Lecturer):
        print(obj)

print("Список студентов")
for obj in gc.get_objects():
    if isinstance(obj, Student):
        print(obj)

print("Сравнение объектов по средним оценкам")
print("student_01 > student_02", student_01 > student_02)
print("lecturer_01 > lecturer_02", lecturer_01 > lecturer_02)
print("student_01 < lecturer_01", student_01 < lecturer_01)
print()

def average_rate_course_std(course, student_list):
    sum_ = 0
    qty_ = 0
    for std in student_list:
        for crs in std.grades:
            std_sum_rate = std.average_rate_course(course)
            sum_ += std_sum_rate
            qty_ += 1
    result = round(sum_ / qty_, 1)
    return result

def average_rate_course_lct(course, lector_list):
    sum_ = 0
    qty_ = 0
    for lct in lector_list:
        for crs in lct.grades:
            lct_sum_rate = lct.average_rate_course(course)
            sum_ += lct_sum_rate
            qty_ += 1
    result = round(sum_ / qty_, 1)
    return result

print("Средняя оценка за домашние задания")
print(average_rate_course_std("Python", student_list))

print("Средняя оценка за лекции")
print(average_rate_course_lct("Python", lector_list))


