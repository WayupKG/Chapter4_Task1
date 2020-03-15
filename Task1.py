class Student:
    def __init__(self, name, surname, god, spes):
    
        self.name = name
    
        self.surname = surname
    
        self.god = god
    
        self.spes = spes
    
    def get_student_info(self):
        print(f"{self.name} {self.surname} поступил в {self.god}г. на факультет: {self.spes}.")

Student_info = Student('Adi', 'Kambarov', '2017', 'Программирование')
Student_info.get_student_info()