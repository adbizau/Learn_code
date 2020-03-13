class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade.score)

    def get_average(self):
        avg = 0
        return sum()


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        if self.score >= Grade.minimum_passing:
            return True
        else:
            return False


# execute
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
x = Grade(60)
pieter.add_grade(x)
pieter.add_grade(Grade(77))

print(pieter.get_average)
pieter.get_average
