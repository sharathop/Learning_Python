class student :

    intrest = 2.0  #instance varibles /class variables
    no_of_students = 0
#  It must be the first parameter of any method inside a class if that method needs to access instance data.

    def __init__(self, Fname,Lname,course,Fees):
        self.Fname = Fname
        self.Lname = Lname
        self.course = course
        self.Fees = Fees

        student.no_of_students += 1

    def Fullname(self):
        return '{} {}'.format(self.Fname, self.Lname)
    

    def fess_cal(self):
        return self.Fees * student.intrest
    
stud1 = student("sharath" , "M", "Machine Learning",50000)
stud2 = student("Tharun" , "R", "Artficial Intelligence",60000)

# print(stud1.intrest)
# print(stud2.intrest)

print(student.Fullname(stud1))

print(student.intrest)

stud1.intrest=1.5
print(stud1.course)
print(student.no_of_students)

print(stud1.no_of_students)
print(stud2.no_of_students)


print(stud1.fess_cal())
print(stud2.fess_cal())
