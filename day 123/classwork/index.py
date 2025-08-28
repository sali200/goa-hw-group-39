
# class Person:
#     def __init__(self, name, surname, age, work):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.work = work

#     def working(self):
#         print(f"{self.name} working at {self.work}")

# class Student(Person):
#     def __init__(self, name, surname, age, work, year):
#         super().__init__(name, surname, age, work)  
#         self.year = year

#     def working(self):
#         print("studying")


class Person:
    def __init__(self, name, surname, age, work, birth_year, id_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.work = work
        self._birth_year = birth_year       
        self.__id = id_number              

    def working(self):
        print(f"{self.name} working at {self.work}")

class Student(Person):
    def __init__(self, name, surname, age, work, birth_year, id_number, year):
        super().__init__(name, surname, age, work, birth_year, id_number)
        self.year = year

    def working(self):
        print("studying")


person1 = Person("arseba", "arsebuli", 35, "Bank ", 1989, "73642")
student1 = Student("arseba", "arasebuli", 20, "TSU", 2004, "8374", 2)


print(person1._birth_year)  

print(person1._Person__id)  
print(student1._Person__id) 