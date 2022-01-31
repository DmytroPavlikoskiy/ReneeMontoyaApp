from models.employee import Employee
from models.plant import Plant
from models.salon import Salon


class Controller:

    def run(self):
        while True:
            print(
                "Choose a menu item by number: \n" +
                "1. Add new Plant \n" +
                "2. Get plant by id \n" +
                "3. Add new Employee \n" +
                "4. Get employee by id \n" +
                "5. Add new Salon \n" +
                "6. Get salon by id \n"
            )
            menu_flag = int(input("Your choose: "))
            if menu_flag == 1:
                self.add_plant()

            elif menu_flag == 2:
                self.get_plant()

            elif menu_flag == 3:
                self.add_employee()

            elif menu_flag == 4:
                self.get_employee()

            elif menu_flag == 5:
                self.add_salon()

            elif menu_flag == 6:
                self.get_salon()

    def add_plant(self):
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        plant = Plant(id, location, name, director_id)
        plant.save()


    def get_plant(self):
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)

    def add_employee(self):
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employees = Employee(id, name, email, department_type, department_id)
        employees.save()


    def get_employee(self):
        id = int(input("ID: "))
        employees = Employee.get_by_id(id)
        print(employees)

    def add_salon(self):
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        name_salon = input("Name Salon:")
        salon = Salon(id, location, name, name_salon)
        salon.save()

    def get_salon(self):
        id = int(input("ID: "))
        salon = Salon.get_by_id(id)
        print(salon)
