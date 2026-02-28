class Student:
    college_name = "Youtube"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def student_details(self):
        print("college:" + self.college_name)
        print("Student Name:"+ self.name)
        print("Marks:",self.marks)

    def student_result(self):
        if(self.marks >= 36):
            print("PASS")
        else:
            print("FAIL")

    def update_marks(self, bonus):
        self.marks += bonus

    @classmethod
    def change_college(cls, newcollege):
        cls.college_name = newcollege

    @staticmethod
    def is_valid_marks(marks):
        if marks < 0 or marks > 100:
            return "invalid"
        return "valid"
        
stud1 =Student("Yuvi" , 63)
stud2 =Student("virat", 35)
stud3 =Student("mahi" , 66)

stud1.student_details()
stud2.student_details()
stud3.student_details()

stud1.student_result()
stud2.student_result()
stud3.student_result()

stud2.update_marks(1)

stud2.student_details()
stud2.student_result()


stud1.college_name="pw"
# print("college:", self.college_name)
stud1.student_details()

print(stud2.is_valid_marks(52))
            


    
































