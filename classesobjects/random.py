class Person:
    def __init__(self, first_name, last_name, age=22):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self):
        return f"Hello {self.first_name} {self.last_name}."


ivan = Person("Ivan", "Ivanov")
maria = Person("Maria", "Ivanova")
plamen = Person("Plamen", "Plamenov")

print(ivan.age)
ivan.age += 1
print(ivan.age)

print(ivan.say_hello())
print(maria.say_hello())
print(plamen.say_hello())

