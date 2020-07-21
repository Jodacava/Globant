class Employee:
    def __init__(self):
        self.employies = []
        self.exec()

    def create(employee_code, name, lastname, address, age, start_date, salary, position, department):
        employee = {
            'employee_code': employee_code,
            'name': name,
            'lastname': lastname,
            'address': address,
            'age': age,
            'start_date': start_date,
            'salary': salary,
            'position': position,
            'department': department
        }
        return employee

    def readfile(self):
        file = open('D:/Johann/Datos/Globant/files/empleados.txt', 'r')
        lines = file.readlines()
        for line in lines:
            cadena = line.split(';')
            listemployee = []
            if cadena[0] != 'employee_code':
                if not cadena[0] in listemployee:
                    listemployee.append(cadena[0])
                    emp = self.create(cadena[0], cadena[1], cadena[2], cadena[3], cadena[4], cadena[5], cadena[6], cadena[7], cadena[8])
                    self.employies.append(emp)

    def lowersalary(self):
        emplowsal = [cod for cod in self.employies if int(cod['salary']) <= 1000000]
        return emplowsal

    def exec(self):
        Employee.readfile(self)
        listemplowsal = Employee.lowersalary(self)
        for emp in listemplowsal:
            print(emp)

if __name__ == "__main__":
    e = Employee()
    print(e)
