#class

class Employee:
    empId=''
    empName=''
    empDepartment=''

#constructor

    def __init__(self,empId,empName,empDepartment):
        self.empId=empId
        self.empName=empName
        self.empDepartment=empDepartment

    def __str__(self):
        return f"Employee Details: {self.empId} : {self.empName} {self.empDepartment}"
    
#create object

suresh=Employee('e201','Suresh CH','Finance')
parul=Employee('e202','Parul Arora','IT')

print(f"{suresh}")
print(parul)
