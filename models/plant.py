from framework.models import Model

class Plant(Model):
    table = 'plant'

    def __init__(self, id, location, name, director_id):
        self.id = id
        self.location = location
        self.name = name
        self.director_id = director_id

    def save(self):
        cursor = self.connects()
        sql = 'INSERT INTO plant(id, location, name, director_id)' \
              ' VALUES ("%s", "%s", "%s", "%s")' % (str(self.id), self.location, self.name, str(self.director_id))
        try:
            cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()