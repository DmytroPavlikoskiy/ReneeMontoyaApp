from framework.models import Model

class Salon(Model):
    table = 'salon'

    def __init__(self, id, location, name, name_salon):
        self.id = id
        self.location = location
        self.name = name
        self.name_salon = name_salon

    def save(self):
        cursor = self.connects()
        sql = 'INSERT INTO salon(id, location, name, name_salon)' \
              ' VALUES ("%s", "%s", "%s", "%s")' % (str(self.id), self.location, self.name, self.name_salon)
        try:
            cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()