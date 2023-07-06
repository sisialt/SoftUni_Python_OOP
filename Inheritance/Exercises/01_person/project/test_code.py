from project.child import Child
from project.person import Person

c = Child("SISI", 2)
print(c.name)

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)