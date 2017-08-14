from .PythonExample import Person, Manager

bob = Person('bob')
sue = Person('Sue', job='dev', pay=100)
tom = Manager('Tom', 5000)


import shelve
db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()
