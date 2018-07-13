class Employee(object):
    
    empCount = 0

    def __initi__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.empCount +=1

    def displayCount(self):
        print("Total Employee %d" % Employee.empcount)

    def displayEmployee(self):
        print("Name: ", self.name, "Salary: ", self.salary)
