from framework.models import Model

class Employee(Model):
    table = 'employees'

    def __init__(self, id, name, email, department_type, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id
        print("Function init employees")

    def save(self):
        cursor = self.connects()
        sql = 'INSERT INTO employees(id, name, email, department_type, department_id) ' \
              'VALUES ("%s", "%s", "%s", "%s", "%s")' % (str(self.id), self.name, self.email, self.department_type, str(self.department_id))
        try:
            cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
