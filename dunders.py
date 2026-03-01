class College:
    college_name = 'MITT'

    def __init__(self, Course, fee):
        self.Course = Course
        self.fee = fee
        
    def details(self):
        print("college:",self.college_name)
        print("Course:",self.Course)
        print("fee:",self.fee)

    def __str__(self):
        return "{}, {}".format(self.college_name,self.Course)

    def __repr__(self):
        return "{}-{}-{}".format(self.Course,self.fee,self.college_name)


cour1= College('MCA', 160000)
cour2=College("MBA", 170000)

print(repr(cour1))
print(str(cour2))

print(cour1.Course.__len__())

print(dir(str))


# cour1.details()
# cour2.details()
