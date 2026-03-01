class Employee:
    bonus= 1.0

    def __init__(self,fName,LName,salary):
        self.fName = fName
        self.LName = LName
        # self.email = fName + LName + '@gmail.com'
        self.salary = salary

    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.fName, self.LName)

    @property
    def full_name(self):
        return '{} {}'.format(self.fName, self.LName)
    
    @full_name.setter
    def full_name(self,name):
        fName, LName = name.split(" ")
        self.fName =fName
        self.LName =LName
    
    @full_name.deleter
    def full_name(Self):
        print("Deleted Name")
        Self.fName = None
        Self.LName = None
    
    def total_salary(self):
       return (self.salary*self.bonus)

    def emp_details(self):
        print(self.full_name)
        print(self.email)
        print(self.total_salary())
    
    def __str__(self):
        return self.full_name
    
    
        
        
# class Devloper(Employee):
#     bonus = 1.12

#     def __init__(self,fName,LName,salary,prog_language):
#         super().__init__(fName,LName,salary)
#         self.prog_language =prog_language

    


# class Manager(Employee):

#     def __init__(self, fName, LName, salary, employess=None):
#         super().__init__(fName, LName, salary)
#         if employess is None:
#             self.employess = []
#         else:
#          self.employess = employess


#     def add_emp(self, emp):
#         if emp not in self.employess:
#             self.employess.append(emp)

#     def remove_emp(self,emp):
#         if emp in self.employess:
#             self.employess.remove(emp)
    
    

#     def emp_under_manager(self):
#         print(f"Manger: {self.full_name()}")
#         print("employess")

#         for emp in self.employess:
#             print(emp)



emp1 = Employee('John' ,'k' ,60000)
emp2 = Employee('jonty', 'g', 70000 )

emp1.emp_details()
# emp2.emp_details()


emp1.full_name='Sharath M'
emp1.emp_details()



del emp1.full_name
emp1.emp_details()

print("name")
print(emp1.fName)



# print("------------------------------------------------")
# dev1 = Devloper('Naman','Mortal', 80000, 'Python')
# dev2 = Devloper('Mamba', 'Ahmed', 90000,'Java')

# dev1.emp_details()
# dev2.emp_details()


    

# print("------------------------------------------------")


# mang1 = Manager('Rebel', 'ali', 100000)
# mang2 = Manager('Sid', 'Joshi', 150000)





# mang1.add_emp(emp1)
# mang2.add_emp(dev1)
# mang1.add_emp(dev2)
# mang2.add_emp(emp2)

# mang1.emp_details()
# mang2.emp_details()

# print("------------------------------------------------")



# mang1.emp_under_manager()
# mang2.emp_under_manager()


# print(isinstance(mang1,Employee))
# print(issubclass(Manager,Employee))
    










# # print(dev1.email)




       

    


# # print(emp1.full_name())
# # print(emp2.email)
# # emp2.total_salary()
# # print(emp2.salary)

