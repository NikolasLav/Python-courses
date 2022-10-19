import random

class Student:

    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.aw_rate = 0

        
    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                lecturer.aw_rate_count()
            else:
                lecturer.grades[course] = [grade]
                lecturer.aw_rate_count() 
        else:
            return 'Ошибка'

    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


    def aw_rate_count(self):
        all_rates = []
        for rates in self.grades.values():
            all_rates += rates
        self.aw_rate = round(sum(all_rates) / len(all_rates), 2)
            
    
    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.aw_rate}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress )}\nЗавершенные курсы: {', '.join(self.finished_courses)}"


    def __le__(self, other):
        if isinstance(other, Student):
            return self.aw_rate <= other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')


    def __lt__(self, other):
        if isinstance(other, Student):
            return self.aw_rate < other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')

    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.aw_rate == other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')
    

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.aw_rate != other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')
    

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.aw_rate > other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')
    

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.aw_rate >= other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')
    

class Mentor:

    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    
    def rate_hw(self, student, course, grade):
        if isinstance(
                self, Reviewer
        ) and isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.aw_rate_count()
            else:
                student.grades[course] = [grade]
                student.aw_rate_count()
        else:
            return 'Ошибка'


class Lecturer(Mentor):


    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] 
        self.grades = {}
        self.aw_rate = 0


    def aw_rate_count(self):
        all_rates = []
        for rates in self.grades.values():
            all_rates += rates
        self.aw_rate = round(sum(all_rates) / len(all_rates), 2)


    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.aw_rate <= other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')


    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.aw_rate < other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')

    
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.aw_rate == other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')
    

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.aw_rate != other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')
    

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.aw_rate > other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')
    

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.aw_rate >= other.aw_rate
        else:
            return print('ошибка!сравниваются разные классы.')

                    
    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.aw_rate}"
        

class Reviewer(Mentor):


    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['HTML+CSS']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', random.randint(1,10))

cool_lector = Lecturer('Gannibal', 'Lector')
cool_lector.courses_attached += ['Python']

best_student.rate_lection(cool_lector, 'Python', 10)
best_student.rate_lection(cool_lector, 'Python', 10)
best_student.rate_lection(cool_lector, 'Python', random.randint(1,10))

random_student = Student('Luis', 'Perenna', 'your_ginger')
random_student.courses_in_progress += ['Python']

random_reviewer = Reviewer('Moes', 'Doby')
random_reviewer.courses_attached += ['Python']

random_reviewer.rate_hw(random_student, 'Python', random.randint(1,10))
cool_reviewer.rate_hw(random_student, 'Python', random.randint(1,10))
random_reviewer.rate_hw(random_student, 'Python', random.randint(1,10))
cool_reviewer.rate_hw(random_student, 'Python', random.randint(1,10))

random_lector = Lecturer('Shelock', 'Holms')
random_lector.courses_attached += ['Python']

best_student.rate_lection(random_lector, 'Python', random.randint(1,10))
random_student.rate_lection(random_lector, 'Python', random.randint(1,10))
best_student.rate_lection(random_lector, 'Python', random.randint(1,10))
random_student.rate_lection(random_lector, 'Python', random.randint(1,10))

print(best_student)
print(best_student.grades)
print(cool_lector)
print(cool_lector.grades)

print(cool_reviewer)

print(random_student.grades)
print(random_student)
print(random_lector.grades)
print(random_lector)
print(random_reviewer)
print()
print('== :',random_student == best_student)
print('!= :',random_student != best_student)
print('>= :',random_student >= best_student)
print('> :',random_student > best_student)
print('<= :',random_student <= best_student)
print('< :',random_student < best_student)
print()
print('== :',random_student == cool_lector)
print()
print('== :',random_lector == cool_lector)
print('!= :',random_lector != cool_lector)
print('>= :',random_lector >= cool_lector)
print('> :',random_lector > cool_lector)
print('<= :',random_lector <= cool_lector)
print('< :',random_lector < cool_lector)
print('== :',random_lector == cool_lector)