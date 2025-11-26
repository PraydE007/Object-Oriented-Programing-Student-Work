class Person:
    def __init__(self, name, age, person_id, email, phone):
        self.name = name
        self.age = age
        self.person_id = person_id
        self.email = email
        self.phone = phone

    def get_contact_info(self):
        return f"Email: {self.email}, Phone: {self.phone}"
    
    def get_full_info(self):
        return f"{self.__class__.__name__} {self.name}, ID: {self.person_id}, Age: {self.age}"
    
    def update_email(self, new_email):
        self.email = new_email
        print(f"Email оновлено для {self.name}")
    
    def update_phone(self, new_phone):
        self.phone = new_phone
        print(f"Телефон оновлено для {self.name}")

class Student(Person):
    def __init__(self, name, age, person_id, email, phone):
        super().__init__(name, age, person_id, email, phone)
        self.group = None
        self.grades = []
        self.scholarship = 0
    
    def add_grade(self, subject, grade):
        self.grades.append({"subject": subject, "grade": grade})
    
    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(g["grade"] for g in self.grades) / len(self.grades)
    
    def set_scholarship(self, amount):
        self.scholarship = amount


class Teacher(Person):
    def __init__(self, name, age, person_id, email, phone):
        super().__init__(name, age, person_id, email, phone)
        self.department = None
        self.subjects = []
        self.salary = 0
        self.experience_years = 0
    
    def add_subject(self, subject):
        self.subjects.append(subject)
    
    def set_salary(self, amount):
        self.salary = amount
    
    def get_salary_info(self):
        bonus = self.experience_years * 1000
        return f"Salary: {self.salary}, Bonus: {bonus}, Total: {self.salary + bonus}"


class Administrator(Person):
    
    def __init__(self, name, age, person_id, email, phone):
        super().__init__(name, age, person_id, email, phone)
        self.position = None
        self.department = None
        self.salary = 0
        self.access_level = 1
    
    def set_position(self, position):
        self.position = position
    
    def set_access_level(self, level):
        if 1 <= level <= 5:
            self.access_level = level
    
    def grant_access(self, resource):
        if self.access_level >= 3:
            return f"{self.name} має доступ до {resource}"
        return f"{self.name} не має достатнього рівня доступу"


class Librarian(Person):
    def __init__(self, name, age, person_id, email, phone):
        super().__init__(name, age, person_id, email, phone)
        self.shift = None
        self.books_issued = []
        self.salary = 0
    
    def issue_book(self, book_title, person_name):
        self.books_issued.append({"book": book_title, "person": person_name})
        return f"Книга '{book_title}' видана для {person_name}"
    
    def get_issued_books_count(self):
        return len(self.books_issued)


# Використання
student = Student("Оксана Петренко", 19, "S001", "oksana@college.com", "+380501234567")
student.set_scholarship(2000)
student.add_grade("Математика", 95)
student.add_grade("Програмування", 90)

teacher = Teacher("Ігор Коваленко", 45, "T001", "igor@college.com", "+380502345678")
teacher.add_subject("Програмування")
teacher.add_subject("Бази даних")
teacher.set_salary(25000)
teacher.experience_years = 15

admin = Administrator("Марина Сидоренко", 38, "A001", "marina@college.com", "+380503456789")
admin.set_position("Завідувач навчальної частини")
admin.set_access_level(4)

librarian = Librarian("Петро Мельник", 52, "L001", "petro@college.com", "+380504567890")
librarian.shift = "денна"
librarian.issue_book("Python для початківців", "Оксана Петренко")

# Виведення
print(student.get_full_info())
print(student.get_contact_info())
print(f"Середній бал: {student.get_average_grade()}")

print("\n" + teacher.get_full_info())
print(teacher.get_contact_info())
print(teacher.get_salary_info())

print("\n" + admin.get_full_info())
print(admin.grant_access("База даних студентів"))

print("\n" + librarian.get_full_info())
print(f"Видано книг: {librarian.get_issued_books_count()}")